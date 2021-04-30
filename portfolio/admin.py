from django.contrib import admin
from .models import Portfolio, PortfolioImage


# 이미지 클래스는 inline
class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage

# 게시글 클래스는 해당하는 이미지 객체를 리스트로 관리하는 형태
class PortfolioAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for img in request.FILES.getlist('images'):
            obj.productimage_set.create(image_url=img)
    inlines = [PortfolioImageInline, ]

# Register your models here.
admin.site.register(Portfolio, PortfolioAdmin)