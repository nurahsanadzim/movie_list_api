"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dokumentasi, name="dokumentasi"),
    path('profil/', views.profil, name="profil"),
    path('daftar/', views.daftar, name="daftar"),
    path('login/', auth_views.LoginView.as_view(template_name='masuk.html'), name='login'),
    path('keluar/', auth_views.logout_then_login, name='keluar'),
    path('movie_id/<int:movie_id>', views.movie_id, name='movie_id'),
    path('jumlah_movie/<int:amount>', views.jumlah_movie, name='jumlah_movie'),
    path('tambah_movie/', views.tambah_movie, name='tambah_movie'),
    path('edit_movie/', views.edit_movie, name='edit_movie'),
]
