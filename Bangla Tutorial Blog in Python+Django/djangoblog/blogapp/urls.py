from django.urls import path
from . import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('author/<name>', views.getauthor, name="author"),
    path('article/<int:id>', views.getsingle, name="single_post"),
    path('topic/<name>', views.getTopic, name="topic"),
    path('create', views.getCreate, name="create"),
    path('profile', views.getProfile, name="profile"),
    path('update/<int:pid>', views.getUpdate, name="update"),
    path('delete/<int:pid>', views.getDelete, name="delete"),
    path('login', views.getLogin, name="login"),
    path('logout', views.getLogout, name="logout"),

    path('register', views.getRegister, name="register"),
    path('topic', views.getCategory, name="category"),
    path('create/topic', views.createTopic, name="createTopic"),
]


# project/urls.py
#handler404 = 'blogapp.views.handler404'