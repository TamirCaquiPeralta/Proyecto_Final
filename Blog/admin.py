from django.contrib import admin
from Blog.models import Blog
from Accounts.models import Avatar

admin.site.register(Avatar)
admin.site.register(Blog)
