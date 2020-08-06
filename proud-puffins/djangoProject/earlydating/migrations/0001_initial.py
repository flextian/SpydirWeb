# Generated by Django 3.0.8 on 2020-08-06 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import earlydating.puffin_functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('img', models.ImageField(default='/static/images/Proud_Puffin_default_user.jpg', null=True, upload_to='static/user_pixel', validators=[earlydating.puffin_functions.validate_file_size])),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('preference', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Both', 'Both')], max_length=10, null=True)),
                ('lower_age', models.PositiveSmallIntegerField(null=True)),
                ('upper_age', models.PositiveSmallIntegerField(null=True)),
                ('bio', models.TextField(default='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_vote', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'voter')},
            },
        ),
    ]
