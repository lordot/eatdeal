# Generated by Django 4.1.7 on 2023-04-20 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_promo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
