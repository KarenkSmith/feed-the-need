# Generated by Django 2.1.5 on 2019-03-17 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190316_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='neededitem',
            name='date',
            field=models.DateField(default=datetime.date(2019, 3, 16)),
        ),
    ]