from django.urls import path
from .views import *

urlpatterns = [
    path('init/', create_table),
]