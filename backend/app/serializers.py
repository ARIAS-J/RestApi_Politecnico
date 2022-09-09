from rest_framework import serializers
from .models import Alumno, Grado, Materia, Profesor, Aula, Turno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alumno
        fields='__all__'
        
        # extra_kwargs = {}


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profesor
        fields='__all__'
        
        # extra_kwargs = {}


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aula
        fields='__all__'
        
        # extra_kwargs = {}


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Materia
        fields='__all__'
        
        # extra_kwargs = {}


class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grado
        fields='__all__'
        
        # extra_kwargs = {}


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Turno
        fields='__all__'
        
        # extra_kwargs = {}