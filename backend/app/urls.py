from django.urls import path
from .views import AlumnoList, AlumnoRetrieve, AsignarAula, ProfesorList, ProfesorRetrieve, AulaList, AulaRetrieve, TurnoList, TurnoRetrieve


urlpatterns = [
    # Alumnos Routes
    path('alumnos/', AlumnoList),
    path('alumnos/<int:pk>', AlumnoRetrieve ),
    
    # Profesores Routes
    path('profesores/', ProfesorList),
    path('profesores/<str:Nombre>', ProfesorRetrieve ),
    
    # Aulas Routes
    path('aulas/', AulaList),
    path('aulas/<int:pk>', AulaRetrieve),
    
    # Turnos Routes
    path('turnos/', TurnoList),
    path('turnos/<int:pk>', TurnoRetrieve),
    
    # Asignar
    path('asignar_aula/<int:pk>', AsignarAula),
    
]