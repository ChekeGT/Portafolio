from django.urls import path
from .views import  PortfolioDetailView, PortfolioListView
urlpatterns = [
    path('portfolio/', PortfolioListView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/<slug:slug>', PortfolioDetailView.as_view(), name='portfolio_detail')
]