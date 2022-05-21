from django.urls import path
from .views import *

urlpatterns = [
    path('django/', django_view, name='django'),
    path('display/', display_view, name='display'),
    path('templates/', templates_view, name='templates'),
]