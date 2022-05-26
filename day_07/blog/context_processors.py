from django.contrib.auth.forms import AuthenticationForm


def base_login(request):
    form = AuthenticationForm()
    return {'login': form}
