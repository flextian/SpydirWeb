# Generated by Django 3.0.8 on 2020-08-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20200804_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='topic',
            field=models.CharField(default='General', max_length=50),
        ),
    ]
