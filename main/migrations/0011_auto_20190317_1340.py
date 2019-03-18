# Generated by Django 2.1.5 on 2019-03-17 20:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_auto_20190317_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=250)),
                ('contact_info', models.TextField(max_length=250)),
                ('org_description', models.TextField(max_length=250)),
                ('org_url', models.URLField(max_length=250)),
                ('wish_list', models.URLField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='neededitem',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 17, 20, 40, 18, 309402, tzinfo=utc)),
        ),
    ]
