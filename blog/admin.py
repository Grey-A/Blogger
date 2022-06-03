from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Post, Category, Subscribe

# Register your models here.
admin.site.register(Post)

admin.site.register(Category)

admin.site.register(Subscribe)

# Unregistered Models
admin.site.unregister(Group)