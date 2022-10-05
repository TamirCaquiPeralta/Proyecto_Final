from email.mime import base
from django.contrib import admin
from django.urls import path
from Blog import views 

urlpatterns = [
    path('', views.inicio, name= "inicio"),

    path('sobre_nosotros/', views.sobre_nosotros, name= "sobre_nosotros"),

    path('blog/', views.BlogList.as_view(), name= "blog"),
    
    path('crear/', views.crear_blog, name="crear"),
    
    path('masinfo/<int:pk>/', views.BlogDetail.as_view(), name="mas_info"),
    
    path('editar/<int:pk>/', views.BlogUpdate.as_view(), name="editar"),
    
    path('eliminar/<int:pk>/', views.BlogDelete.as_view(), name="eliminar"),


]