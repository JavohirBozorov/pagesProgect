from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SettingsPageView(TemplateView):
    template_name = 'settings.html'

class PrisingPageView(TemplateView):
    template_name = 'prising.html'