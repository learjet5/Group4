# Generated by Django 3.0.3 on 2020-05-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('User_Profile', '0005_auto_20200506_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
