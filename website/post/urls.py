from django.urls import path
from .views import *

urlpatterns = [

    path('list/', post_list, name="url_post_list"),
    path('create/', post_create, name="url_post_create"),
    path('read/<int:pk>', post_read, name="url_post_read"),
    path('update/<int:pk>', post_update, name="url_post_update"),
    path('delete/<int:pk>', post_delete, name="url_post_delete"),
    
]