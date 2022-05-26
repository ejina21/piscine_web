from django.urls import path
from .views import HomePageView, ArticleView, SignUpView, PublicationView, ArticleDetailView, \
    FavouritesView, CreateArticleView, AddFavouriteArticleView, SetLangView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticleView.as_view(), name='articles'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('publications/', PublicationView.as_view(), name='publication'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('favourite/', FavouritesView.as_view(), name='favourite'),
    path('publish/', CreateArticleView.as_view(), name='publish'),
    path('add_to_favourite/<int:pk>/', AddFavouriteArticleView.as_view(), name='add_fav'),
    path('set_lang/<slug:slug>/', SetLangView.as_view(), name='set_lang')
]