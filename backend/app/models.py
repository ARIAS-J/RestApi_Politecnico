from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Alumno(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    matricula = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    edad = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(20)])
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Matricula: {self.Matricula} Alumno:{self.nombre} {self.apellido}"

class Profesor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    edad = models.IntegerField(validators=[MinValueValidator(21)])
    numero_telefonico = models.CharField(max_length=35)

    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null = True)
    
    def __str__(self):
        return f"Docente: {self.nombre} {self.apellido} Numero Telefonico:{self.numero_telefonico}"

class Aula(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    seccion = models.CharField(max_length=1)
    capacidad = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    
    #Relationship
    id_grado = models.ForeignKey("Grado", on_delete=models.CASCADE, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Seccion de aula: {self.seccion} Capacidad:{self.capacidad}/30"


class Materia(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre_materia = models.CharField(max_length=35)
    
    #Relationship
    id_profesor = models.ForeignKey("Profesor", on_delete=models.CASCADE, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Materia: {self.nombre_materia}"


class Grado(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    grado = models.CharField(max_length=20)
    
    #Relationship
    id_materia = models.ForeignKey("Materia", on_delete=models.CASCADE, null=True, blank=True)
    id_alumno = models.ForeignKey("Alumno", on_delete=models.CASCADE, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Grado: {self.grado}"


class Turno(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    hora_de_inicio = models.TimeField()
    hora_de_finalizacion = models.TimeField()
    
    #Relationship
    id_profesor = models.ForeignKey("Profesor", on_delete=models.CASCADE, null=True, blank=True)
    id_materia = models.ForeignKey("Materia", on_delete=models.CASCADE, null=True, blank=True)
    id_aula = models.ForeignKey("Aula", on_delete=models.CASCADE, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)