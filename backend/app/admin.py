from django.contrib import admin
from .models import Alumno, Profesor, Aula

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Aula)