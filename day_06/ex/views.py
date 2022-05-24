import random

from django.shortcuts import render
from django.views.generic import TemplateView

from day_06.settings import USER_NAMES


class HomePageView(TemplateView):
    template_name = 'home.html'


