# Generated by Django 3.2.15 on 2022-11-01 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0010_alter_instrument_locker_assignment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instrument",
            name="locker_assignment",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="inventory.locker",
            ),
        ),
    ]