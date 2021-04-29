from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

from .apps import HomeConfig as config

app_name = config.name
urlpatterns = [
    path('', views.IndexView.as_view(), name='homeIndex'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)