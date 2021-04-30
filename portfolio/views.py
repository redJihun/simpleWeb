from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView

from .forms import PortfolioForm
from bookmark.models import Bookmark

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

# class ReadPortfolio(TemplateView):
#     template_name = 'portfolio/detail.html'
#     def get(self, request, portfolio_id):
#         portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
#         return render(request, self.template_name, {'portfolio_detail': portfolio_detail})

class ReadPortfolio(DetailView):
    template_name = "portfolio/detail.html"
    form_class = PortfolioForm
    def get(self, request):
        form = self.form_class()
        return render()
    
