# Generated by Django 3.1 on 2020-08-09 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20200808_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 14, 10, 19, 669171, tzinfo=utc)),
        ),
    ]
