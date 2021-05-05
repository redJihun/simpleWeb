from django.urls import path

from . import views

from .apps import PortfolioConfig as config

app_name = config.name
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    # path('new/', views.NewPortfolio.as_view(), name='new'),
    path('create/', views.CreatePortfolio.as_view(), name='create'),
    path('detail/<int:portfolio_id>', views.detail , name='detail'),
    path('<int:pk>/update/', views.UpdatePortfolio.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeletePortfolio.as_view(), name='delete')
]