# Generated by Django 2.1.5 on 2019-03-17 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeededItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('location', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='what',
            field=models.CharField(max_length=100, verbose_name='select an item'),
        ),
        migrations.AddField(
            model_name='neededitem',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Item'),
        ),
    ]
