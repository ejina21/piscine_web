from django.urls import path
from chat.views import *

urlpatterns = [
    path('', LinksView.as_view(), name='home'),
    path('login/', LoginPage.as_view(), name='login'),
    path('<int:pk>/', RoomView.as_view(), name='chat'),
    path('logout/', Logout.as_view(), name='logout'),
]