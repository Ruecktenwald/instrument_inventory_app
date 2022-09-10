# Generated by Django 3.2.15 on 2022-09-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0016_auto_20220904_0143"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lock",
            name="lock_code",
        ),
        migrations.AddField(
            model_name="lock",
            name="combination_number",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name="lock",
            name="lock_serial_number",
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
