from django.conf.urls import url
from .import views

app_name= "productapp"

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^insert$', views.insert,name='insert'),
    url(r'^details$', views.details,name='details'),
    url(r'^update$', views.update,name='update'),
    url(r'^delete$', views.delete,name='delete')
]