from django.urls import path
from .views import HomePageView, SignUpView, DeleteTipView, UpvoteView, DownvoteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('remove/<int:pk>/', DeleteTipView.as_view(), name='remove'),
    path('upvote/<int:pk>/', UpvoteView.as_view(), name='upvote'),
    path('downvote/<int:pk>/', DownvoteView.as_view(), name='downvote'),

]