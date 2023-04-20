# Generated by Django 4.1.7 on 2023-04-20 03:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_alter_city_utc_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='favorited',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
