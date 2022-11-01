from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.inventory.models import Instrument
import csv


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        return

    with open("orchard_gardens_inventory.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # next(csv_reader)
        instrument_total = 0

        for line in csv_reader:

            Instrument.objects.create(
                instrument_name=line["instrument_name"],
                serial_number=line["serial_number"],
                condition=line["condition"],
                mouth_piece_accessory=line["mouth_piece_accessory"],
                ligature_accessory=line["ligature_accessory"],
                cork_grease_accessory=line["cork_grease_accessory"],
                reeds_accessory=line["reeds_accessory"],
                case_accessory=line["case_accessory"],
                notes=line["notes"],
                instrument_kind=line["instrument_kind"],
                locker_assignment_id=line["locker_assignment_id"],
                student_id=line["student_id"],
            )
            instrument_total += 1

        print(f"{instrument_total} instruments created!")
