from django.urls import path

from . import views

from .apps import PortfolioConfig as config

app_name = config.name
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='portfolioIndex'),
    path('create/', views.CreatePortfolio.as_view(), name='create'),
    path('detail/<int:portfolio_id>', views.ReadPortfolio.as_view(), name='read'),
]