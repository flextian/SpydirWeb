# Generated by Django 3.0.8 on 2020-08-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhoneNumber',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
