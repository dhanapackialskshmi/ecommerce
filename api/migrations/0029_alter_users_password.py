# Generated by Django 3.2.7 on 2021-09-23 05:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20210923_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('([A-Z]+)([a-z])([0-9]+)($|?|!){8}', message='Password is Invalid.')]),
        ),
    ]