from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Alumno, Profesor, Aula, Turno
from .serializers import AlumnoSerializer, AsignarAulaSerializer, ProfesorSerializer, AulaSerializer, TurnoSerializer

# Alumno Views

# "swagger_auto_schema" decorator Returns a path parameter schema to the user.
@swagger_auto_schema(methods=['post'], request_body=AlumnoSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def AlumnoRetrieve(request, alumno_id = None):
    # Queryset - Obtiene un alumno especifico.
    alumno = Alumno.objects.filter(id = alumno_id).first()
    
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def AulaRetrieve(request, aula_id = None):
    # Queryset - Obtiene un aula especifica.
    aula = Aula.objects.filter(id = aula_id).first()
    
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


# Turnos Views

@swagger_auto_schema(methods=['post'], request_body=TurnoSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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
            
            aula_id = serializer.data['id_aula']
            
            hora_a_registrar = serializer.data['hora']
            
            profesor_id = serializer.data['id_profesor']

            turnos_registrados_aula = Turno.objects.filter(id_aula = aula_id)
            
            for turno in turnos_registrados_aula:
                if hora_a_registrar == str(turno.hora):
                    return Response({'message':'No se puede asignar el turno.'})

            turnos_registrados_profesor = Turno.objects.filter(id_profesor = profesor_id)
            
            for turno in turnos_registrados_profesor:
                if hora_a_registrar == str(turno.hora):
                    return Response({'message':'No se puede asignar el turno.'})
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=TurnoSerializer)
@api_view(['GET','PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def TurnoRetrieve(request, turno_id = None):
    # Queryset - Obtiene un turno especifico.
    turno = Turno.objects.filter(id = turno_id).first()
    
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

# Asignar Aula Views

@swagger_auto_schema(methods=['put'], request_body=AsignarAulaSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def AsignarAula(request, alumno_id = None):
    alumno = Alumno.objects.filter(id = alumno_id).first()

    if not alumno: return Response({'message':'No se ha encontrado un alumno'})
        
    if request.method != 'PUT': return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) 
    
    serializer = AlumnoSerializer(alumno, data=request.data)
    
    # Validacion
    if not serializer.is_valid(): return Response(serializer.errors) 
        
    data = serializer.validated_data
    
    aula_id = data['id_aula'].id
    
    alumnos_registrados = Alumno.objects.filter(id_aula = aula_id).count()
    
    aula = AulaSerializer(Aula.objects.get(id = aula_id))
    
    if alumnos_registrados < aula.data['capacidad']:
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        return Response({'message': 'No se pudo asignar. El aula esta completa'})
