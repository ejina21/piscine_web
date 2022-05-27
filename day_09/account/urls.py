from django.urls import path
from account.views import AccountView, custom_logout

urlpatterns = [
    path('login/', AccountView.as_view(), name='account'),
    path('logout/', custom_logout, name='logout')
]