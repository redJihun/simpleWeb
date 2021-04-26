from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def index(request):
#     return HttpResponse('portfolio index')

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)