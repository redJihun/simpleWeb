from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.template import RequestContext

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
            print(request.FILES.getlist('images'))
            for img in request.FILES.getlist('images'):
                print(img)
                portfolio_image = PortfolioImage()
                portfolio_image.portfolio_id = temp.id
                portfolio_image.image = img
                portfolio_image.save()
            
        else:
            return redirect('portfolio:create')
            
        return redirect('portfolio:detail',temp.id)

    def get(self, request, *args, **kwargs):
        portfolio = self.portfolio_class()
        return render(request, self.template_name, {'form': portfolio})


def detail(request, portfolio_id):
    template_name = "portfolio/detail.html"
    portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
    building_type = '상업시설' if portfolio_detail.buildingType=='C' else( '주거복합' if portfolio_detail.buildingType=='R' else '주택' ) 
    portfolio_image = portfolio_detail.portfolioimage_set.all()
    
    return render(request, template_name, {'portfolio_detail': portfolio_detail, 'building_type': building_type, 'portfolio_image': portfolio_image})

class UpdatePortfolio(UpdateView):
    template_name = 'portfolio/update.html'
    form_class = PortfolioForm
    context_object_name = 'portfolio'
    success_url='/portfolio/'

    def get_object(self):
        portfolio = get_object_or_404(Portfolio, pk=self.kwargs['pk'])
        portfolio_images = portfolio.portfolioimage_set.all()
        # building_type = '상업시설' if portfolio.buildingType=='C' else( '주거복합' if portfolio.buildingType=='R' else '주택' ) 
        # for img in request.FILES.getlist('images'):
        #     portfolio_image = PortfolioImage()
        #     portfolio_image.portfolio_id = portfolio.id
        #     portfolio_image.image = img
        #     portfolio_image.save()

        return portfolio
    
    # def post(self, request, *args, **kwargs):
    #     portfolio = get_object_or_404(Portfolio, pk=self.kwargs['pk'])
        
    #     for img in request.FILES.getlist('images'):
    #         portfolio_image = PortfolioImage()
    #         portfolio_image.portfolio_id = portfolio.id
    #         portfolio_image.image = img
    #         portfolio_image.save()
            
    #     return portfolio

class DeletePortfolio(DeleteView):
    template_name = 'portfolio/delete.html'
    model = Portfolio
    success_url = '/portfolio/'
    context_object_name = 'portfolio'

    # def get_object(self):
    #     portfolio = get_object_or_404(Portfolio, pk=self.kwargs['pk'])
    #     return portfolio