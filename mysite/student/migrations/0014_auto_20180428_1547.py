# Generated by Django 2.0.4 on 2018-04-28 15:47

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20180428_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=student.models.upload_location),
        ),
    ]
