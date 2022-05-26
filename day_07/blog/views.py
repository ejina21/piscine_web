from django.views.generic import ListView, RedirectView, CreateView, DetailView
from django.urls import reverse_lazy, reverse
from blog.models import Article, UserFavouriteArticle
from blog.forms import UserCreationForm, ArticleForm, UserFavouriteArticleForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import IntegrityError
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class AnonRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return super(AnonRequiredMixin, self).dispatch(request, *args, **kwargs)


class HomePageView(RedirectView):
    pattern_name = 'articles'


class ArticleView(ListView):
    template_name = 'home.html'
    context_object_name = 'articles'
    queryset = Article.objects.all().order_by('-created')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return super(SignUpView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse_lazy('login'))
        return render(request, self.template_name, {'form': form})


class PublicationView(LoginRequiredMixin, ListView):
    template_name = 'publication.html'
    context_object_name = 'articles'
    login_url = 'login'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'art'
    template_name = 'detail.html'


class FavouritesView(LoginRequiredMixin, ListView):
    template_name = 'favourite.html'
    context_object_name = 'articles'
    login_url = 'login'

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user)


class CreateArticleView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'publish.html'
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, self.template_name, {'form': form})


class AddFavouriteArticleView(CreateView):
    form_class = UserFavouriteArticleForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        new_article = form.save(commit=False)
        new_article.user = request.user
        new_article.article = Article.objects.get(pk=kwargs['pk'])
        try:
            new_article.save()
        except IntegrityError:
            pass
        return HttpResponseRedirect(reverse_lazy('favourite'))


class SetLangView(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        settings.LANGUAGE_CODE = kwargs['slug']
        return reverse(self.pattern_name)
