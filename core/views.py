import json
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from core.serializers import MovieSerializer
from core.models import Movie


def dokumentasi(request):
    return render(request, 'dokumentasi.html')

@login_required
def profil(request):
    user_token = Token.objects.get(user=request.user)
    return render(
        request, 'profil.html',
        {'token': user_token}
    )

def daftar(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        # login otomatis setelah mendaftar
        user = authenticate(username=username, password=password)
        login(request, user)
        # generate token untuk user yang sudah mendaftar
        Token.objects.create(user=request.user)
        # redirect user baru ke home
        return redirect('profil')
    return render(request, 'daftar.html', {'form': form})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_id(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        data = 'Tidak menemukan movie dengan id tersebut!, mungkin sudah terhapus atau tidak tersedia.'
    else:
        data = {
            'id': movie.id,
            'title': movie.title,
            'overview': movie.overview,
            'genres': [g['name'] for g in json.loads(movie.genres)] if movie.genres != '-' else '-',
            'release_date': movie.release_date,
            'runtime': movie.runtime + ' menit' if movie.runtime != '-' else '-',
            'original_language': movie.original_language,
            'popularity': movie.popularity,
            'homepage': movie.homepage
        }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def jumlah_movie(request, amount):
    query_result = Movie.objects.all()[:amount]
    data = [
        {
            'id': movie.id,
            'title': movie.title,
            'overview': movie.overview,
            'genres': [g['name'] for g in json.loads(movie.genres)] if movie.genres != '-' else '-',
            'release_date': movie.release_date,
            'runtime': movie.runtime + ' menit' if movie.runtime != '-' else '-',
            'original_language': movie.original_language,
            'popularity': movie.popularity,
            'homepage': movie.homepage
        }
        for movie in query_result
    ]
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tambah_movie(request):
    movie = request.data.dict()
    if 'title' in movie:
        # handle jika ada genres
        if 'genres' in movie:
            movie['genres'] = json.dumps([ {'name':g} for g in movie['genres'].split(',')])
        # parse dengan serializer Movie untuk di validasi
        serializer = MovieSerializer(data=movie)
        if serializer.is_valid():
            # simpan ke database
            serializer.save()      
            return Response(
                'Data berhasil disimpan, id data yang disimpan: ' + str(serializer.data['id']) + '.',
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Mohon tambahkan required body parameter 'title'.")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_movie(request):
    movie = request.data.dict()
    if 'id' in movie:
        try:
            to_edit = Movie.objects.get(pk=movie['id'])
        except Movie.DoesNotExist:
            return Response(
                'Data dengan id tersebut tidak ditemukan.', 
                status=status.HTTP_404_NOT_FOUND
            )

        if 'genres' in movie:
            movie['genres'] = json.dumps([ {'name':g} for g in movie['genres'].split(',')])
        # hapus id dari dict untuk di update ke database
        del movie['id']
        # update object yang di di update berdasarkan field yang di request
        for field in movie:
            setattr(to_edit, field, movie[field])
        # simpan hasil perubahan object ke database
        to_edit.save()
        return Response('Data berhasil diupdate.')
    else:
        return Response("Mohon tambahkan required body parameter 'id'.")