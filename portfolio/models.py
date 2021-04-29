from django.db import models
from django.contrib.auth.models import User

import os
from uuid import uuid4
from django.utils import timezone

# Create your models here.

def date_upload_to(instance, filename):
    id = models.BigAutoField(primary_key=True)
    # upload_to = 년 월 일 날짜로 세분화
    ymd_path = timezone.now().strftime('portfolio/%Y/%m/%d')
    # 길이 32일 uuid 값
    uuid_name = uuid4().hex
    # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
    # 결합 후 리턴
    return '/'.join([
        ymd_path,
        uuid_name + extension,
    ])

class Portfolio(models.Model):
    """Model definition for MODELNAME."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    # TODO: Define fields here
    title = models.CharField(max_length = 50, default='-')
    location = models.CharField(max_length = 100, default='-')
    service = models.CharField(max_length = 20, default='-')
    area = models.CharField(max_length = 20, default='0')
    # photo = models.ImageField(upload_to=date_upload_to)

    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio', blank=True, null=True)
