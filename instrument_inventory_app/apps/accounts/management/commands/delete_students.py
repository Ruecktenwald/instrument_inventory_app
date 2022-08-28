from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.accounts.models import Student


class Command():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    Student.objects.all().delete()

    print("All students deleted!")
