from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)