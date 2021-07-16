# Generated by Django 3.2.4 on 2021-07-15 17:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PBL', '0006_auto_20210714_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 22, 30, 41, 231463)),
        ),
    ]
