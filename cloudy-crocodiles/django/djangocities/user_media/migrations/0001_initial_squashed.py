# Generated by Django 3.0.9 on 2020-08-05 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocities.user_media.models


class Migration(migrations.Migration):

    replaces = [('user_media', '0001_initial'), ('user_media', '0002_auto_20200803_0315')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=djangocities.user_media.models.upload_to)),
                ('description', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user_media',
            },
        ),
    ]
