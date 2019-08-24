"""Henrique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core.views import listar, cadastro, deletar, atualizar
from core.views import publicos_listar, publico_cadastrar, publico_atualizar, publico_deletar
from django.conf import settings
from django.conf.urls.static import static

#OUTRA COISA
from core.views import index, perfil, registro, dados
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Documentos
    path('doc/', listar, name='doc'),
    path('cadastro/', cadastro, name='cadastro'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('deletar/<int:id>/', deletar, name='deletar'),
    path('admin/', admin.site.urls),

    #Publicos
    path('publicos/', publicos_listar, name='publicos'),
    path('publico_cadastrar/', publico_cadastrar, name='publico_cadastrar'),
    path('publico_atualizar/<int:id>/', publico_atualizar, name='publico_atualizar'),
    path('publico_deletar/<int:id>/', publico_deletar, name='publico_deletar'),


    #OUTRA COISA
    path('', index, name='index'),

    #Perfil
    path('perfil/', perfil, name='perfil'),

    #Registro de usuário
    path('registro/', registro, name='registro'),
    path('dados/<int:id>/', dados, name='dados'),

    #Autentificação
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(),
    name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
