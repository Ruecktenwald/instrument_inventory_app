# Generated by Django 3.2.15 on 2022-08-31 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20220830_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='locker_number',
            field=models.CharField(max_length=3, null=True),
        ),
    ]