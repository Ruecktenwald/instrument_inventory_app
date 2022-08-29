from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.accounts.models import Student
import csv


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        return

    with open('students.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        next(csv_reader)
        student_total = 0
        sum = 0
        for line in csv_reader:

            Student.objects.create(first_name=line['first_name'], last_name=line['last_name'])
            sum +=1

        print(f"{sum} students created!")
