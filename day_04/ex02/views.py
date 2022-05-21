from django.shortcuts import render

from .forms import MyForm
from django.conf import settings
import datetime


def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            with open(settings.LOG_PATH, 'a') as f:
                time = datetime.datetime.now()
                f.write(f'[{time}] {form.cleaned_data["text"]}\n')
            with open(settings.LOG_PATH, 'r') as f:
                history = f.read()
            return render(request, 'admin/ex02/index.html', context={'form': form, 'history': history})
    else:
        try:
            with open(settings.LOG_PATH, 'r') as f:
                history = f.read()
        except Exception:
            with open(settings.LOG_PATH, 'x'):
                history = ''
        form = MyForm()
    return render(request, 'admin/ex02/index.html', context={'form': form, 'history': history})