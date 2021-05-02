from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse

from .forms import PortfolioForm, PortfolioImageForm
from .models import Portfolio, PortfolioImage

# Create your views here.

# def index(request):
#     return HttpResponse('portfolio index')

def index(request):
    template_name = 'portfolio/index.html'
    portfolios = Portfolio.objects.all()
    return render(request, template_name, {'portfolios':portfolios})

# class NewPortfolio(TemplateView):
#     template_name = 'portfolio/create.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)


class CreatePortfolio(CreateView):
    template_name = 'portfolio/create.html'
    portfolio_class = PortfolioForm   
    portfolio_image_class = PortfolioImageForm 
    def post(self, request, *args, **kwargs):
        portfolio = self.portfolio_class(request.POST)
        # portfolio.title = request.POST['title']
        # portfolio.buildingType = request.POST['buildingType']
        # portfolio.location = request.POST['location']
        # portfolio.service = request.POST['service']
        # portfolio.area = request.POST['area']
        if portfolio.is_valid():
            temp = portfolio.save()
            for img in request.FILES.getlist('images'):
                portfolio_image = self.portfolio_image_class(portfolio=portfolio, image=img)
                # portfolio_image.portfolio = portfolio
                # portfolio_image.image = img
                if portfolio_image.is_valid():
                    portfolio_image.save()
                    # return redirect(reverse('portfolio:detail', args=))
                else:
                    return redirect('portfolio:create')
            return redirect('portfolio:detail',temp.id)
        else:
            return redirect('portfolio:create')
    def get(self, request, *args, **kwargs):
        portfolio = self.portfolio_class()
        return render(request, self.template_name, {'form': portfolio})

# class ReadPortfolio(TemplateView):
#     template_name = 'portfolio/detail.html'
#     def get(self, request, portfolio_id):
#         portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
#         return render(request, self.template_name, {'portfolio_detail': portfolio_detail})

# class ReadPortfolio(DetailView):
#     template_name = "portfolio/detail.html"
#     # form_class = PortfolioForm
#     def get(self, request):
#         # form = self.form_class()
#         portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
#         # return render(request, self.template_name, {'portfolio_detail': portfolio_detail})
#         return render(request, self.template_name, {'portfolio_detail': portfolio_detail})
    
def detail(request, portfolio_id):
    template_name = "portfolio/detail.html"
    portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
    # portfolio_image = get_object_or_404(PortfolioImage, portfolio=portfolio_detail)
    return render(request, template_name, {'portfolio_detail': portfolio_detail})