# Generated by Django 3.2.7 on 2021-09-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_users_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='users',
            name='mobile_no',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
