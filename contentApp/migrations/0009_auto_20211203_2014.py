# Generated by Django 3.2.8 on 2021-12-03 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentApp', '0008_auto_20211203_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='name',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 20, 14, 8, 595407)),
        ),
    ]
