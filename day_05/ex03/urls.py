from django.urls import path
from .views import *

urlpatterns = [
    path('populate/', insert_data),
    path('display/', get_data)
]