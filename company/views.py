from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'company/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)