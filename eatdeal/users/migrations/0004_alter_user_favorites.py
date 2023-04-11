# Generated by Django 4.1.7 on 2023-04-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_city_utc_time'),
        ('users', '0003_alter_user_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorited', to='api.promo'),
        ),
    ]