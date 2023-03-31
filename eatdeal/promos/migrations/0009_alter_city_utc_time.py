# Generated by Django 4.1.7 on 2023-03-31 05:26

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('promos', '0008_alter_city_utc_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='utc_time',
            field=timezone_field.fields.TimeZoneField(use_pytz=True),
        ),
    ]
