from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import PortfolioForm

# Create your views here.

# def index(request):
#     return HttpResponse('portfolio index')

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class CreatePortfolio(TemplateView):
    template_name = 'portfolio/create.html'
    form_class = PortfolioForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('IndexView')
        else:

            return redirect('IndexView')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

