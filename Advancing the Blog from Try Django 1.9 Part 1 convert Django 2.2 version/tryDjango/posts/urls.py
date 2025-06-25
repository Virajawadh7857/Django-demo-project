from django.urls import path, re_path
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    )
app_name = 'posts'

urlpatterns = [
    path('create/', post_create),
    path('', post_list, name='list'),
    re_path('(?P<slug>[-\w]+)/edit/$', post_update, name='update'),
    re_path('(?P<slug>[-\w]+)/delete/$', post_delete, name='delete'),
    re_path('(?P<slug>[-\w]+)/$', post_detail, name='detail'),

]
