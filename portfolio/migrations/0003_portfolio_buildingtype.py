# Generated by Django 3.2 on 2021-05-01 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_portfolio_buildingtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='buildingType',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]