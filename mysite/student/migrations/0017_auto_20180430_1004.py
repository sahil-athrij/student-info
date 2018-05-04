# Generated by Django 2.0.4 on 2018-04-30 10:04

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20180430_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admtype',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Lateral Entry', 'Lateral Entry')], default='Regular', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=student.models.upload_location),
        ),
    ]
