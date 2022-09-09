from rest_framework import serializers
from .models import Alumno, Grado, Materia, Profesor, Aula, Turno

class AlumnoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Alumno
        fields=('id', 'matricula', 'nombre', 'apellido', 'edad', 'id_grado', 'created_at', 'updated_at')
        
        # extra_kwargs = {}


class ProfesorSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Profesor
        fields=('id', 'nombre', 'apellido', 'edad', 'numero_telefonico', 'is_active', 'created_at', 'updated_at', 'deleted_at')
        
        # extra_kwargs = {}


class AulaSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Aula
        fields=('id', 'seccion', 'capacidad', 'id_grado', 'created_at', 'updated_at')
        
        # extra_kwargs = {}


class MateriaSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Materia
        fields=('id', 'nombre_materia', 'id_profesor', 'id_grado' 'created_at', 'updated_at')
        
        # extra_kwargs = {}


class GradoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Grado
        fields=('id', 'grado', 'created_at', 'updated_at')
        
        # extra_kwargs = {}


class TurnoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Turno
        fields=('id', 'hora_de_inicio', 'hora_de_finalizacion', 'id_profesor', 'id_materia', 'id_aula', 'created_at', 'updated_at')
        
        # extra_kwargs = {}