from django.shortcuts import render
from django.views.generic import TemplateView
from .models import People, Planets


class DisplayView(TemplateView):
    template_name = 'ex09/display.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = People.objects.filter(homeworld__climate__in='windy').order_by('name')
        print(context['context'])
        return context
