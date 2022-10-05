from email.mime import base
from telnetlib import LOGOUT
from django.contrib import admin
from django.urls import path
from Accounts import views
urlpatterns = [
 
path('iniciar_sesion/', views.login_request, name= "iniciar_sesion"),
 
path('register/', views.register, name="registrate" ),

path('logout/', views.CustomLogoutView.as_view(), name="cerrar_sesion" ),

path('editar_perfil', views.ProfileUpdateView.as_view(), name="editar_perfil"),

 ]