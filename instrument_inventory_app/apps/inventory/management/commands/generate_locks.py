from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.inventory.models import Lock
import csv


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        return

    with open("locks.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        next(csv_reader)
        student_total = 0
        sum = 0
        for line in csv_reader:

            Lock.objects.create(
                lock_serial_number=line["lock_serial_number"],
                combination_number=line["combination_number"],
                id=line["lock_serial_number"],
            )
            sum += 1

        print(f"{sum} locks created!")
