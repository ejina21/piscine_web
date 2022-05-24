from django.urls import path
from .views import *

urlpatterns = [
    path('init/', create_table),
    path('populate/', insert_data),
    path('display/', get_data),
    path('remove/', remove_data, name='remove')
]