from django.contrib import admin
from .models import Categories, Units, Products

# Register your models here.

admin.site.register(Categories)
admin.site.register(Units)
admin.site.register(Products)
