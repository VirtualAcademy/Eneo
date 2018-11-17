# Generated by Django 2.1.3 on 2018-11-15 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0009_auto_20181115_1124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supply',
            options={'verbose_name': 'Supply', 'verbose_name_plural': 'Supplies'},
        ),
        migrations.AddField(
            model_name='supply',
            name='destined_to',
            field=models.ForeignKey(default=0, help_text='The fuel storage unit.', on_delete=django.db.models.deletion.CASCADE, to='fuel.Powerplant', verbose_name='Fuel Receptacle'),
            preserve_default=False,
        ),
    ]
