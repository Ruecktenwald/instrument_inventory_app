# Generated by Django 3.2.15 on 2022-11-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_instrument_locker_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='instrument_kind',
            field=models.CharField(choices=[('oboe', 'oboe'), ('flute', 'flute'), ('clarinet', 'clarinet'), ('bass clarinet', 'bass clarinet'), ('bassoon', 'bassoon'), ('alto sax', 'alto sax'), ('tenor sax', 'tenor sax'), ('baritone sax', 'baritone sax'), ('trumpet', 'trumpet'), ('french horn', 'french horn'), ('trombone', 'trombone'), ('baritone horn', 'baritone horn'), ('bass guitar', 'bass guitar'), ('percussion', 'percussion')], max_length=64, null=True),
        ),
    ]
