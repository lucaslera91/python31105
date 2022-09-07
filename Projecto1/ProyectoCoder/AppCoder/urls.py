from django.urls import path
from AppCoder import views


urlpatterns = [
    # path('familiares', views.familiares),
    path('cursos', views.cursos, name="cursos"),
    path('', views.inicio, name="inicio"),
    path('profesores', views.profesores, name="profesores"),
    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('entregables', views.entregables, name="entregables"),

]