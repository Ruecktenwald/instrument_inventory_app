# Generated by Django 3.2.15 on 2022-08-30 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0007_auto_20220830_0547"),
    ]

    operations = [
        migrations.RenameField(
            model_name="instrument",
            old_name="polishing_cloth",
            new_name="polishing_cloth_accessory",
        ),
    ]
