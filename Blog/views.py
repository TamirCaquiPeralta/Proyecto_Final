from django.shortcuts import render

def inicio (request):
    return render(request,"Blog/inicio.html")
    
def sobre_nosotros(request): 
    return render(request, "Blog/sobre_nosotros.html" )

def blog(request): 
    return render(request, "Blog/blog.html")
    