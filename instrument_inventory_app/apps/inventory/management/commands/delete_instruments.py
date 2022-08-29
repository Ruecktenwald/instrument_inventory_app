from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.inventory.models import Instrument


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        pass

    Instrument.objects.all().delete()

    print("All instruments deleted!")
