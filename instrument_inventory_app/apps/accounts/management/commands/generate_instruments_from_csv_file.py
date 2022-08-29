from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.accounts.models import Instrument
import csv

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        return

    with open('accounts_instrument.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        #next(csv_reader)
        instrument_total = 0

        for line in csv_reader:

            Instrument.objects.create(instrument_name=line['instrument_name'],serial_number=line['serial_number'],condition=line['condition'],mouth_piece=line['mouth_piece'],ligature=line['ligature'],cork_grease=line['cork_grease'],reeds=line['reeds'],case=line['case'],notes=line['notes'],instrument_category_id=line['instrument_category_id'],locker_assignment_id=line['locker_assignment_id'],student_id=line['student_id'])
            instrument_total +=1

        print(f"{instrument_total} instruments created!")
