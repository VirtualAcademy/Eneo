# Generated by Django 2.1.3 on 2018-11-22 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='production',
            options={'verbose_name': 'Production', 'verbose_name_plural': 'Productions'},
        ),
        migrations.AlterField(
            model_name='production',
            name='time_recorded',
            field=models.TimeField(default=datetime.datetime.today),
        ),
    ]
