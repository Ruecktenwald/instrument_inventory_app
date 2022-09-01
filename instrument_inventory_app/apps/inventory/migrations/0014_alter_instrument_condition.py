# Generated by Django 3.2.15 on 2022-09-01 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20220901_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='condition',
            field=models.CharField(blank=True, choices=[('broken', 'broken'), ('needs repair soon', 'needs repair soon'), ('decent condition', 'decent condition'), ('excellent condition', 'excellent condition'), ('in repair shop', 'in repair shop')], default='decent condition', max_length=64, null=True),
        ),
    ]
