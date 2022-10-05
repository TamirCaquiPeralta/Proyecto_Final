from django import forms
from Blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields = ['titulo','subtitulo','cuerpo']
