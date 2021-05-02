from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .apps import LoginConfig as config

app_name = config.name
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]