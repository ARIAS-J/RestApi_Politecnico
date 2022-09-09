from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Alumno, Grado, Materia, Profesor, Aula, Turno
from .serializers import AlumnoSerializer, ProfesorSerializer, AulaSerializer, MateriaSerializer, GradoSerializer, TurnoSerializer

# Alumno Views

# "swagger_auto_schema" decorator Returns a path parameter schema to the user.
@swagger_auto_schema(methods=['post'], request_body=AlumnoSerializer)
@api_view(['GET', 'POST'])
def AlumnoList(request):
    # List - Muestra Todos los alumnos.
    if request.method == 'GET':
        # Queryset
        alumnos = Alumno.objects.all()
        # Serializer
        serializer = AlumnoSerializer(alumnos,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create - Crea un alumno nuevo.
    elif request.method == 'POST':
        serializer = AlumnoSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=AlumnoSerializer)
@api_view(['GET','PUT', 'DELETE'])
def AlumnoRetrieve(request, pk = None):
    # Queryset - Obtiene un alumno especifico.
    alumno = Alumno.objects.filter(id = pk).first()
    
    # Validacion
    if alumno:
        
        # Retrieve - Retorna toda la informacion del alumno especificado.
        if request.method == 'GET':
            # Serializer
            serializer = AlumnoSerializer(alumno)
            return Response(serializer.data)

        # Update - Actualiza la informacion del alumno especificado.
        elif request.method == 'PUT':
            # Serializer   
            serializer = AlumnoSerializer(alumno, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        # Delete - Elimina al alumno especificado
        elif request.method == 'DELETE':
            alumno.delete()
            return Response({'message':'Alumno eliminado correctamente'}, )

    return Response({'message':'No se ha encontrado un alumno'})


# Profesor Views

@swagger_auto_schema(methods=['post'], request_body=ProfesorSerializer)
@api_view(['GET', 'POST'])
def ProfesorList(request):
    # List - Muestra Todos los profesores.
    if request.method == 'GET':
        # Queryset
        profesores = Profesor.objects.all()
        # Serializer
        serializer = ProfesorSerializer(profesores,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create - Crea un profesor nuevo.
    elif request.method == 'POST':
        serializer = ProfesorSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=ProfesorSerializer)
@api_view(['GET','PUT', 'DELETE'])
def ProfesorRetrieve(request, Nombre = None):
    # Queryset - Obtiene un profesor especifico.
    profesor = Profesor.objects.filter(nombre = Nombre).first()
    
    # Validacion
    if profesor:
        
        # Retrieve - Retorna toda la informacion del profesor especificado.
        if request.method == 'GET':
            # Serializer
            serializer = ProfesorSerializer(profesor)
            return Response(serializer.data)

        # Update - Actualiza la informacion del profesor especificado.
        elif request.method == 'PUT':
            # Serializer   
            serializer = ProfesorSerializer(profesor, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        # Delete - Elimina al profesor especificado
        elif request.method == 'DELETE':
            profesor.delete()
            return Response({'message':'Profesor eliminado correctamente'}, )

    return Response({'message':'No se ha encontrado un profesor'})


# Aulas Views

@swagger_auto_schema(methods=['post'], request_body=AulaSerializer)
@api_view(['GET', 'POST'])
def AulaList(request):
    # List - Muestra Todas las aulas.
    if request.method == 'GET':
        # Queryset
        aulas = Aula.objects.all()
        # Serializer
        serializer = AulaSerializer(aulas,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create - Crea un aula nueva.
    elif request.method == 'POST':
        serializer = AulaSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=AulaSerializer)
@api_view(['GET','PUT', 'DELETE'])
def AulaRetrieve(request, Seccion = None):
    # Queryset - Obtiene un aula especifica.
    aula = Aula.objects.filter(seccion = Seccion).first()
    
    # Validacion
    if aula:
        
        # Retrieve - Retorna toda la informacion del aula especificada.
        if request.method == 'GET':
            # Serializer
            serializer = AulaSerializer(aula)
            return Response(serializer.data)

        # Update - Actualiza la informacion del aula especificada.
        elif request.method == 'PUT':
            # Serializer   
            serializer = AulaSerializer(aula, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        # Delete - Elimina el aula especificado
        elif request.method == 'DELETE':
            aula.delete()
            return Response({'message':'Aula eliminada correctamente'}, )

    return Response({'message':'No se ha encontrado un aula'})


# Materias Views

@swagger_auto_schema(methods=['post'], request_body=MateriaSerializer)
@api_view(['GET', 'POST'])
def MateriaList(request):
    # List - Muestra Todas las materias.
    if request.method == 'GET':
        # Queryset
        materias = Materia.objects.all()
        # Serializer
        serializer = MateriaSerializer(materias,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create - Crea una materia nuevo.
    elif request.method == 'POST':
        serializer = MateriaSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=MateriaSerializer)
@api_view(['GET','PUT', 'DELETE'])
def MateriaRetrieve(request, Nombre_Materia = None):
    # Queryset - Obtiene una materia especifica.
    materia = Materia.objects.filter(nombre_materia = Nombre_Materia).first()
    
    # Validacion
    if materia:
        
        # Retrieve - Retorna toda la informacion de la materia especificada.
        if request.method == 'GET':
            # Serializer
            serializer = MateriaSerializer(materia)
            return Response(serializer.data)

        # Update - Actualiza la informacion de la materia especificada.
        elif request.method == 'PUT':
            # Serializer   
            serializer = MateriaSerializer(materia, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        # Delete - Elimina la materia especificado
        elif request.method == 'DELETE':
            materia.delete()
            return Response({'message':'Materia eliminada correctamente'}, )

    return Response({'message':'No se ha encontrado una materia'})


# Grados Views

@swagger_auto_schema(methods=['post'], request_body=GradoSerializer)
@api_view(['GET', 'POST'])
def GradoList(request):
    # List - Muestra Todos los grados.
    if request.method == 'GET':
        # Queryset
        grados = Grado.objects.all()
        # Serializer
        serializer = GradoSerializer(grados,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create - Crea un grado nuevo.
    elif request.method == 'POST':
        serializer = GradoSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=GradoSerializer)
@api_view(['GET','PUT', 'DELETE'])
def GradoRetrieve(request, Grado = None):
    # Queryset - Obtiene un grado especifico.
    grado = Grado.objects.filter(grado = Grado).first()
    
    # Validacion
    if grado:
        
        # Retrieve - Retorna toda la informacion del grado especificado.
        if request.method == 'GET':
            # Serializer
            serializer = GradoSerializer(grado)
            return Response(serializer.data)

        # Update - Actualiza la informacion del grado especificado.
        elif request.method == 'PUT':
            # Serializer   
            serializer = GradoSerializer(grado, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        # Delete - Elimina el grado especificado
        elif request.method == 'DELETE':
            grado.delete()
            return Response({'message':'Grado eliminado correctamente'}, )

    return Response({'message':'No se ha encontrado un grado'})


# Turnos Views

@swagger_auto_schema(methods=['post'], request_body=TurnoSerializer)
@api_view(['GET', 'POST'])
def TurnoList(request):
    # List - Muestra Todos los turnos.
    if request.method == 'GET':
        # Queryset
        turnos = Turno.objects.all()
        # Serializer
        serializer = TurnoSerializer(turnos,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create - Crea un turno nuevo.
    elif request.method == 'POST':
        serializer = TurnoSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=TurnoSerializer)
@api_view(['GET','PUT', 'DELETE'])
def TurnoRetrieve(request, pk = None):
    # Queryset - Obtiene un turno especifico.
    turno = Grado.objects.filter(id = pk).first()
    
    # Validacion
    if turno:
        
        # Retrieve - Retorna toda la informacion del turno especificado.
        if request.method == 'GET':
            # Serializer
            serializer = TurnoSerializer(turno)
            return Response(serializer.data)

        # Update - Actualiza la informacion del turno especificado.
        elif request.method == 'PUT':
            # Serializer   
            serializer = TurnoSerializer(turno, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        # Delete - Elimina el turno especificado.
        elif request.method == 'DELETE':
            turno.delete()
            return Response({'message':'Turno eliminado correctamente'}, )

    return Response({'message':'No se ha encontrado un turno'})