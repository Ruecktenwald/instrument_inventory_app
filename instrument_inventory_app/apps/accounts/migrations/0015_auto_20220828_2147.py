# Generated by Django 3.2.15 on 2022-08-28 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_locker_locker_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='locker_number',
            field=models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.locker'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='student',
            field=models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.student'),
        ),
    ]
