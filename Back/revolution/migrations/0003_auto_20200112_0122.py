# Generated by Django 3.0.2 on 2020-01-12 00:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revolution', '0002_auto_20200111_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='improvement_of',
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 12, 1, 22, 34, 190796)),
        ),
    ]