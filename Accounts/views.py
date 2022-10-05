from urllib import request
from django.shortcuts import render, redirect
from Accounts.form import UserRegisterForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.models import User


def login_request(request):
    next_url = request.GET.get('next')

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            if user:
                login(request=request, user=user)
                
                if next_url:
                    
                    return redirect(next_url)
               
                return render(request, "Blog/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
           
            else:
                return render(request,"Accounts/iniciar_sesion.html", {"mensaje":"Error, ingresaste mal los datos"})
        else:
            return render(request,"Accounts/iniciar_sesion.html", {"mensaje":"Error, datos incorrectos"})

    formulario = AuthenticationForm()
    return render(request,"Accounts/iniciar_sesion.html", {'form':formulario} )
    

def register (request): 
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

      
            form.save()
            return render(request, "Blog/inicio.html", {"mensaje": "Usuario Creado"})
        else:
            mensaje = 'Algo salio mal en el registro, vuelve a intentarlo'
    formulario = UserRegisterForm()  
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "Accounts/registrate.html", context=context)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("iniciar_sesion") 

class ProfileUpdateView(LoginRequiredMixin, UpdateView ):
    model = User 
    form_class = UserUpdateForm
    success_url = reverse_lazy("editar_perfil")
    template_name = "Accounts/editar_perfil.html"
    def get_object(self, queryset = None):
        return self.request.user

        