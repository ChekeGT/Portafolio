from django.urls import path
from .views import  PortfolioDetailView, PortfolioListView
urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio'),
    path('<int:pk>/<slug:slug>', PortfolioDetailView.as_view(), name='portfolio_detail')
]