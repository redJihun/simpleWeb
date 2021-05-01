from .models import Portfolio, PortfolioImage
from django import forms

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'buildingType', 'location', 'service', 'area', ]


class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['image', ]