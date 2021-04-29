from django.urls import path

from . import views

from .apps import BusinessConfig as config

app_name = config.name
urlpatterns = [
    path('', views.IndexView.as_view(), name='businessIndex'),
]