from django.views.generic import ListView, View, DetailView, RedirectView, FormView
from chat.models import Chat
from django.contrib.admin.forms import AuthenticationForm
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


class LinksView(ListView):
    model = Chat
    template_name = 'links.html'
    context_object_name = 'chats'


class RoomView(DetailView):
    model = Chat
    template_name = 'chat.html'
    context_object_name = 'chat'


class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class LoginPage(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = 'home'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return HttpResponseRedirect(reverse('home'))
        return render(request, self.template_name, {'form': form})