from rest_framework import serializers
from .models import Alumno, Profesor, Aula, Turno

class AlumnoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Alumno
        fields=('id', 'matricula', 'nombre', 'apellido', 'edad', 'id_aula', 'created_at', 'updated_at')
        extra_kwargs = {'created_at': {'required': False}, 'updated_at': {'required': False}}

class ProfesorSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Profesor
        fields=('id', 'nombre', 'apellido', 'materia', 'is_active', 'created_at', 'updated_at', 'deleted_at')
        
        # extra_kwargs = {}


class AulaSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Aula
        fields=('id', 'seccion', 'capacidad', 'created_at', 'updated_at')
        
        # extra_kwargs = {}


class TurnoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Turno
        fields=('id', 'hora', 'id_profesor', 'id_aula', 'created_at', 'updated_at')
        
        # extra_kwargs = {}


class AsignarAulaSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Alumno
        fields=('id_aula','updated_at')
        extra_kwargs = {'matricula': {'required': False}, 'nombret': {'required': False}, 'apellido': {'required': False}, 'edad': {'required': False}, 'updated_At': {'required': False}, 'updated_At': {'required': True}}