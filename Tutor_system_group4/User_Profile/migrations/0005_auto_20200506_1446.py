# Generated by Django 3.1 on 2020-05-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('User_Profile', '0004_auto_20200505_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]