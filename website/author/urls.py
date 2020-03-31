from django.urls import path
from .views import *

urlpatterns = [
    
    path('list/', author_list, name="url_author_list"),
    path('create/', author_create, name="url_author_create"),
    path('read/<int:pk>', author_read, name="url_author_read"),
    path('update/<int:pk>', author_update, name="url_author_update"),
    path('delete/<int:pk>', author_delete, name="url_author_delete"),
    
]