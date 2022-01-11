# Generated by Django 3.2.1 on 2022-01-11 00:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 1, 11, 0, 44, 19, 637364, tzinfo=utc))),
            ],
        ),
    ]