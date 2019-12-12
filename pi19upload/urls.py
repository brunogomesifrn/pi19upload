
from django.contrib import admin
from django.urls import path
from core.views import listar, cadastro, deletar, atualizar, area
from core.views import tipo_listar, tipo_cadastrar, tipo_atualizar, tipo_deletar
from django.conf import settings
from django.conf.urls.static import static

#LONGIN
from core.views import index, perfil, registro, dados, filtrar
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Documentos
    path('doc/', listar, name='doc'),
    path('cadastro/', cadastro, name='cadastro'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('deletar/<int:id>/', deletar, name='deletar'),
    path('admin/', admin.site.urls),

    #tipo
    path('tipo/', tipo_listar, name='tipo'),
    path('tipo_cadastrar/', tipo_cadastrar, name='tipo_cadastrar'),
    path('tipo_atualizar/<int:id>/', tipo_atualizar, name='tipo_atualizar'),
    path('tipo_deletar/<int:id>/', tipo_deletar, name='tipo_deletar'),

    #area
    path('area/', area, name='area'),

    #OUTRA COISA
    path('', index, name='index'),

    #Perfil
    path('perfil/', perfil, name='perfil'),

    #Registro de usuário
    path('registro/', registro, name='registro'),
    path('dados/<int:id>/', dados, name='dados'),

    #Autentificação
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('loginsuperuser/', auth_views.LoginView.as_view(), name='loginsuperuser'),
    path("logout/", auth_views.LogoutView.as_view(),
    name="logout"),
    path("filtrar/<int:categoria_id>/",filtrar, name="filtrar")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
