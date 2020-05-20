# Generated by Django 3.1 on 2020-05-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0002_auto_20200520_1541'),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetail',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coursedetail',
            name='student_applied',
            field=models.ManyToManyField(blank=True, related_name='applied_Student', to='User_Profile.Student', verbose_name='申请学员'),
        ),
    ]