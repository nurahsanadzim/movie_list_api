import json
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from .models import Movie

def dokumentasi(request):
    return render(request, 'dokumentasi.html')

@login_required
def profil(request):
    usertoken = Token.objects.get(user=request.user)
    return render(request, 'profil.html' ,{
        'token': usertoken
    })

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
        movie_data = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        data = 'Tidak menemukan movie dengan id tersebut!'
    else:
        data = {
            'judul': movie_data.title,
            'overview': movie_data.overview,
            'genre': [g['name'] for g in json.loads(movie_data.genres)],
            'rilis': movie_data.release_date,
            'durasi': str(int(float(movie_data.runtime))) + ' menit',
            'bahasa': movie_data.original_language,
            'popularitas': movie_data.popularity,
            'homepage': movie_data.homepage
        }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def jumlah_movie(request, amount):
    query_result = Movie.objects.all()[:amount]
    data = [
        {
            'id': movie.id,
            'judul': movie.title,
            'overview': movie.overview,
            'genre': [g['name'] for g in json.loads(movie.genres)],
            'rilis': movie.release_date,
            'durasi': str(int(float(movie.runtime))) + ' menit',
            'bahasa': movie.original_language,
            'popularitas': movie.popularity,
            'homepage': movie.homepage
        }
        for movie in query_result
    ]
    return Response(data)