# Generated by Django 3.2.7 on 2021-09-22 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_users_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile_no',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(max_length=20),
        ),
    ]
