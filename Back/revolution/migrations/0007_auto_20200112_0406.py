# Generated by Django 3.0.2 on 2020-01-12 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revolution', '0006_auto_20200112_0400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initiative',
            name='improvements',
        ),
        migrations.AddField(
            model_name='initiative',
            name='subinitiatives',
            field=models.ManyToManyField(blank=True, default=None, related_name='_initiative_subinitiatives_+', to='revolution.Initiative'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 12, 4, 6, 41, 998378)),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(default=None, to='revolution.Tag'),
        ),
    ]
