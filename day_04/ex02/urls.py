from django.urls import path
from .views import *

urlpatterns = [
    path('', form_view, name='form'),
]