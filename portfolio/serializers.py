from rest_framework import serializers

from portfolio.models import Portfolio, PortfolioImage

class PortfolioImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PortfolioImage
        fields = ['image']

class Portfolio(serializers.ModelSerializer):
    images = PortfolioImageSerializer(many=True, read_only=True)

    class meta:
        model = Portfolio
        fields = ['id', 'title', 'location', 'service', 'area', ]