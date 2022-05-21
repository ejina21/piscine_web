from django.urls import path
from .views import *

urlpatterns = [
    path('', my_table_color_view, name='color'),
]