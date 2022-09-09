from django.urls import path
from .views import AlumnoList, AlumnoRetrieve, ProfesorList, ProfesorRetrieve, AulaList, AulaRetrieve, MateriaList, MateriaRetrieve, GradoList, GradoRetrieve, TurnoList, TurnoRetrieve


urlpatterns = [
    # Alumnos Routes
    path('alumnos/', AlumnoList),
    path('alumnos/<int:pk>', AlumnoRetrieve ),
    
    # Profesores Routes
    path('profesores/', ProfesorList),
    path('profesores/<str:Nombre>', ProfesorRetrieve ),
    
    # Aulas Routes
    path('aulas/', AulaList),
    path('aulas/<str:Seccion>', AulaRetrieve),
    
    # Materias Routes
    path('materias/', MateriaList),
    path('materias/<str:Nombre_Materia>', MateriaRetrieve),
    
    # Grados Routes
    path('grados/', GradoList),
    path('grados/<str:Grado>', GradoRetrieve),
    
    # Turnos Routes
    path('turnos/', TurnoList),
    path('turnos/<int:pk>', TurnoRetrieve),
    
]