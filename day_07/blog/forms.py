from django.forms import ModelForm, CharField, PasswordInput, ValidationError
from django.contrib.auth.models import User
from django import forms

from blog.models import Article, UserFavouriteArticle


class UserCreationForm(ModelForm):
    username = CharField(label='Username', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = CharField(label='Password', widget=PasswordInput(attrs={'class': "form-control"}))
    password2 = CharField(label='Password', widget=PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Password not identical')
        return cd['password2']


class ArticleForm(ModelForm):
    title = CharField(label='Title', widget=forms.TextInput(attrs={'class': "form-control"}))
    synopsis = CharField(label='Synopsis', widget=forms.TextInput(attrs={'class': "form-control"}))
    content = CharField(label='Content', widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Article
        exclude = ['author', 'created']


class UserFavouriteArticleForm(ModelForm):
    class Meta:
        model = UserFavouriteArticle
        exclude = ['user', 'article']