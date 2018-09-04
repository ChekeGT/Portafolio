from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'
class AboutTemplateView(TemplateView):
    template_name = 'core/about.html'


class ContactTemplateView(TemplateView):
    template_name = 'core/contact.html'
