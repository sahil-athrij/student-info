# Generated by Django 2.0.4 on 2019-05-04 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190504_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 11, 43, 23, 161682, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 11, 43, 23, 156098, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='rollnoregnomap',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 11, 43, 23, 162290, tzinfo=utc)),
        ),
    ]
