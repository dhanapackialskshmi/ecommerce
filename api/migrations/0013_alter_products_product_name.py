# Generated by Django 3.2.7 on 2021-09-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]