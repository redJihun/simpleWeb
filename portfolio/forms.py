from .models import Portfolio, PortfolioImage

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['content', ]

class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['file', ]