# Generated by Django 3.1.7 on 2021-10-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pi_commander', '0003_relay_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relay',
            name='name',
        ),
        migrations.AlterField(
            model_name='relay',
            name='label',
            field=models.CharField(default='Relay 1', max_length=40),
        ),
    ]
