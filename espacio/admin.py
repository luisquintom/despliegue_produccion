from django.contrib import admin

# Register your models here.
from .models import Agencia, Mision

# visualmente en el panel
admin.site.register(Agencia)
admin.site.register(Mision)