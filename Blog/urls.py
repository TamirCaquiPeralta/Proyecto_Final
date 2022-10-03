from email.mime import base
from django.contrib import admin
from django.urls import path
from Blog import views 

urlpatterns = [
    path('', views.inicio, name= "inicio"),

    path('sobre_nosotros', views.sobre_nosotros, name= "sobre_nosotros"),

    path('blog', views.blog, name= "blog"),
    
]