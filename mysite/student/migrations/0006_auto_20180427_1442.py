# Generated by Django 2.0.4 on 2018-04-27 14:42

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20180427_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=student.models.upload_location),
        ),
    ]
