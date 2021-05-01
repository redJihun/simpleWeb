from django.db import models

import os
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import User

# from ckeditor.fields import RichTextUploadingField

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
    # id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    # TODO: Define fields here
    title = models.CharField(max_length = 50, default='', null=True)
    buildingType = models.CharField(max_length = 1, choices=(('C','상업시설'), ('R','주거복합'), ('H','주택')),blank=True, null=True)
    location = models.CharField(max_length = 100, default='', null=True)
    service = models.CharField(max_length = 20, default='', null=True)
    area = models.CharField(max_length = 20, default='', null=True)
    # photo = models.ImageField(upload_to=date_upload_to)

    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='portfolio', blank=True, null=True)
    
