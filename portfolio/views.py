from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse

from .forms import PortfolioForm, PortfolioImageForm
from .models import Portfolio, PortfolioImage

# Create your views here.

def index(request):
    template_name = 'portfolio/index.html'
    portfolios = reversed(Portfolio.objects.all())
    return render(request, template_name, {'portfolios':portfolios})


class CreatePortfolio(CreateView):
    template_name = 'portfolio/create.html'
    portfolio_class = PortfolioForm   
    portfolio_image_class = PortfolioImageForm 
    def post(self, request, *args, **kwargs):
        portfolio = self.portfolio_class(request.POST)
        portfolio.data._mutable = True
        portfolio.data['area'] = str(portfolio.data.get('area') + '㎡')
        portfolio.data._mutable = False
        if portfolio.is_valid():
            temp = portfolio.save()
            for img in request.FILES.getlist('images'):
                # portfolio_image = self.portfolio_image_class(request.POST, request.FILES)
                # portfolio_image.data['portfolio'] = temp
                # portfolio_image.data['image'] = img
                # if portfolio_image.is_valid():
                #     portfolio_image.save()
                # else:
                #     return redirect('portfolio:create')
                portfolio_image = PortfolioImage()
                portfolio_image.portfolio = temp
                portfolio_image.image = img
                portfolio_image.save()
            return redirect('portfolio:detail',temp.id)
        else:
            return redirect('portfolio:create')
    def get(self, request, *args, **kwargs):
        portfolio = self.portfolio_class()
        return render(request, self.template_name, {'form': portfolio})


def detail(request, portfolio_id):
    template_name = "portfolio/detail.html"
    portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
    building_type = '상업시설' if portfolio_detail.buildingType=='C' else( '주거복합' if portfolio_detail.buildingType=='R' else '주택' ) 
    portfolio_image = portfolio_detail.portfolioimage_set.all()
    # portfolio_image = get_object_or_404(PortfolioImage, portfolio=portfolio_detail)
    return render(request, template_name, {'portfolio_detail': portfolio_detail, 'building_type': building_type, 'portfolio_image': portfolio_image})