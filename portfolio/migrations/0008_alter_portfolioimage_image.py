# Generated by Django 3.2 on 2021-05-02 02:55

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_portfolio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=portfolio.models.date_upload_to),
        ),
    ]