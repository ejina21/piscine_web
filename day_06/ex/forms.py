from django.forms import ModelForm, CharField, PasswordInput, ValidationError
from django.contrib.auth.models import User
from django import forms

from ex.models import Tip, Upvote


class UpVoteForm(ModelForm):
    class Meta:
        model = Upvote
        fields = ()


class UserCreationForm(ModelForm):
    username = CharField(label='Логин', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': "form-control"}))
    password2 = CharField(label='Подтвердите пароль', widget=PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Пароли не совпадают')
        return cd['password2']


class TipForm(ModelForm):
    content = CharField(label='Контент', widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Tip
        fields = ('content',)