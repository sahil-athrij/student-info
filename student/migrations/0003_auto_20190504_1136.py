# Generated by Django 2.0.4 on 2019-05-04 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190504_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 11, 36, 23, 772046, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 11, 36, 23, 766523, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='rollnoregnomap',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 11, 36, 23, 772648, tzinfo=utc)),
        ),
    ]
