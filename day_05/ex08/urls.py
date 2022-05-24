from django.urls import path
from .views import *

urlpatterns = [
    path('init/', create_table, name='ex08-init'),
    path('populate/', Populate.as_view(), name='ex08-populate'),
    path('display/', Display.as_view(), name='ex08-display'),
]