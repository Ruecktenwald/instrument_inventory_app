# Generated by Django 3.2.15 on 2022-08-28 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_instrument_locker_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='locker_number',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.locker'),
        ),
    ]
