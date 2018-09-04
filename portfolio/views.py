from django.shortcuts import render
from .models import Project
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
class PortfolioListView(ListView):
    model = Project
    template_name = 'portfolio/portfolio_list.html'

class PortfolioDetailView(DetailView):
    model = Project
    template_name = 'portfolio/portfolio_detail.html'