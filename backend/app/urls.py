from django.urls import path
from .views import AlumnoList, AlumnoRetrieve, AsignarAula, ProfesorList, ProfesorRetrieve, AulaList, AulaRetrieve, TurnoList, TurnoRetrieve
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Alumnos Routes
    path('alumnos/', AlumnoList),
    path('alumnos/<int:alumno_id>', AlumnoRetrieve ),
    
    # Profesores Routes
    path('profesores/', ProfesorList),
    path('profesores/<str:Nombre>', ProfesorRetrieve ),
    
    # Aulas Routes
    path('aulas/', AulaList),
    path('aulas/<int:aula_id>', AulaRetrieve),
    
    # Turnos Routes
    path('turnos/', TurnoList),
    path('turnos/<int:turno_id>', TurnoRetrieve),
    
    # Asignar
    path('asignar_aula/<int:alumno_id>', AsignarAula),
    
    # Obtain token route
    path('token/', obtain_auth_token, name='obtain_token'),
]