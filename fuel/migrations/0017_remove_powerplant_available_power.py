# Generated by Django 2.1.3 on 2018-11-22 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0016_auto_20181120_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powerplant',
            name='available_power',
        ),
    ]
