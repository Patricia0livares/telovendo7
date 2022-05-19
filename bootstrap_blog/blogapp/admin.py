from django.contrib import admin
from .models import Cliente, Proveedor,Mensaje
from . import models

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Mensaje)
