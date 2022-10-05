from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User


class Avatar (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    foto = models.ImageField(upload_to = 'avatares', null = True, blank = True) 
    def __str__(self):
        return f'Avatar de: {self.user}'