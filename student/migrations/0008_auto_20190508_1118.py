# Generated by Django 2.0.4 on 2019-05-08 11:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190508_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 11, 18, 22, 557401, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 11, 18, 22, 551862, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='rollnoregnomap',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 11, 18, 22, 558011, tzinfo=utc)),
        ),
    ]
