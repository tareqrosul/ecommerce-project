from django.contrib import admin
from .models import Categories
from .models import Brand
from .models import Products
##Register your models here.
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Products)
