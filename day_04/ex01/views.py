from django.shortcuts import render


def django_view(request):
    return render(request, 'admin/ex01/django.html')


def display_view(request):
    return render(request, 'admin/ex01/display.html')


def templates_view(request):
    return render(request, 'admin/ex01/templates.html')