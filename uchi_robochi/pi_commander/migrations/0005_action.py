# Generated by Django 3.1.7 on 2021-10-20 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pi_commander', '0004_auto_20211019_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('raspberry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi_commander.raspberry')),
                ('relay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi_commander.relay')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
