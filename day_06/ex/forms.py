from django.forms import ModelForm, CharField, PasswordInput, ValidationError
from django.contrib.auth.models import User

from ex.models import Tip, Upvote


class UpVoteForm(ModelForm):
    class Meta:
        model = Upvote
        fields = ()


class UserCreationForm(ModelForm):
    password = CharField(label='Пароль', widget=PasswordInput)
    password2 = CharField(label='Подтвердите пароль', widget=PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Пароли не совпадают')
        return cd['password2']


class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = ('content',)