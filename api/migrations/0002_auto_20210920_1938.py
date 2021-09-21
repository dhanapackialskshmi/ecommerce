# Generated by Django 3.2.7 on 2021-09-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='verified_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='verified_mobile_no',
            field=models.BooleanField(default=False),
        ),
    ]
