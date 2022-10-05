from django.shortcuts import render
from typing import Dict
from urllib import request
from Blog.models import Blog
from Blog.form import BlogForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

def inicio (request):
    return render(request,"Blog/inicio.html")
    
def sobre_nosotros(request): 
    return render(request, "Blog/sobre_nosotros.html" )

def blog(request): 
    return render(request, "Blog/blog.html")
    
class BlogList(ListView):
    model = Blog
    template_name = "Blog/blog.html"


class BlogDelete(LoginRequiredMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('blog')


@login_required
def crear_blog(request):
    if request.method== 'POST':
        form = BlogForm(request.POST,request.FILES)

        if form.is_valid():
            blog= form.save()
            blog.autor= request.user
            blog.save()
            return redirect(reverse('blog'))
    
    else:
        
        form = BlogForm()
    
    return render(request, "Blog/blog_form.html", {"form": form})


class BlogUpdate(LoginRequiredMixin,UpdateView):
    model= Blog
    success_url = reverse_lazy('blog')
    fields= [  'titulo', 'subtitulo', 'cuerpo']


class BlogDetail(DetailView):
    model= Blog
    template_name = "Blog/blog_masinfo.html"

