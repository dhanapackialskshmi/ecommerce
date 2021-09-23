# Generated by Django 3.2.7 on 2021-09-23 05:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20210923_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertracking',
            name='current_location',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator("^[a-zA-Z -.\\'\\_]+$", message='Current Location must be in Letters')]),
        ),
        migrations.AlterField(
            model_name='ordertracking',
            name='destination',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator("^[a-zA-Z -.\\'\\_]+$", message='Destination must be in Letters')]),
        ),
        migrations.AlterField(
            model_name='ordertracking',
            name='shipment_status',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator("^[a-zA-Z -.\\'\\_]+$", message='Status must be in Letters')]),
        ),
    ]