from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='portfolioIndex'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)