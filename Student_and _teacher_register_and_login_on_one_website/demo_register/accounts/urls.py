from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('teacher/', views.Teacher_register, name='Teacher_register'),
    path('student/', views.Student_register, name='Student_register'),
    path('teacher/login/', views.Teacher_loing, name='Teacher_loing'),
    path('teacher/details/', views.Teacher_details, name='Teacher_details'),
    path('teacher/logout/', views.Teacher_logout, name='Teacher_logout'),
    path('student/login/', views.Student_loing, name='Student_loing'),
    path('student/details/', views.Student_details, name='Student_details'),
    path('student/logout/', views.Student_logout, name='Student_logout'),
]
