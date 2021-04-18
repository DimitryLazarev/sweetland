from django.contrib import admin
from django.contrib.auth.models import User
from sweetlandapp.models import Cart, Products

admin.site.register(Cart)
admin.site.register(Products)
