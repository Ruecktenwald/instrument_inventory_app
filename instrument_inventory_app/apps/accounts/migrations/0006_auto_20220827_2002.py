# Generated by Django 3.2.15 on 2022-08-27 20:02

from django.db import migrations, models
import instrument_inventory_app.apps.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_auto_20220827_1957"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="grade",
            field=models.CharField(
                choices=[
                    (
                        instrument_inventory_app.apps.accounts.models.Student.Grades[
                            "fifth"
                        ],
                        "5",
                    ),
                    (
                        instrument_inventory_app.apps.accounts.models.Student.Grades[
                            "sixth"
                        ],
                        "6",
                    ),
                    (
                        instrument_inventory_app.apps.accounts.models.Student.Grades[
                            "seventh"
                        ],
                        "7",
                    ),
                    (
                        instrument_inventory_app.apps.accounts.models.Student.Grades[
                            "eighth"
                        ],
                        "8",
                    ),
                ],
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="homeroom",
            field=models.CharField(
                choices=[
                    (
                        instrument_inventory_app.apps.accounts.models.Student.Homeroom[
                            "o"
                        ],
                        "O",
                    ),
                    (
                        instrument_inventory_app.apps.accounts.models.Student.Homeroom[
                            "g"
                        ],
                        "G",
                    ),
                    (
                        instrument_inventory_app.apps.accounts.models.Student.Homeroom[
                            "p"
                        ],
                        "P",
                    ),
                    (
                        instrument_inventory_app.apps.accounts.models.Student.Homeroom[
                            "s"
                        ],
                        "S",
                    ),
                ],
                max_length=5,
            ),
        ),
    ]
