from django.contrib.admin.forms import AuthenticationForm
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt


class AccountView(FormView):
    form_class = AuthenticationForm
    template_name = 'account/account.html'
    success_url = 'account'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(request, 'account/logout.html')
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
        return HttpResponseRedirect(reverse('account'))


@csrf_exempt
def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('account'))