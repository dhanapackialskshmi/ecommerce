# Generated by Django 3.2.7 on 2021-09-22 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_users_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='phone_number',
        ),
    ]