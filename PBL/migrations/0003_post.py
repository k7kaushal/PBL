# Generated by Django 3.2.4 on 2021-07-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PBL', '0002_auto_20210711_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request1', models.CharField(default='', max_length=100)),
                ('type', models.CharField(choices=[('Stationary', 'Stationary'), ('Notes', 'Notes'), ('Help in Project', 'Help in Project'), ('Other', 'Other')], default='', max_length=20)),
            ],
        ),
    ]
