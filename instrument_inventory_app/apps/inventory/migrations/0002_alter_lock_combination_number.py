# Generated by Django 3.2.15 on 2022-10-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lock",
            name="combination_number",
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
