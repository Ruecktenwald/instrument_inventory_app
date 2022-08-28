from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.accounts.models import Instrument


class Command():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    Instrument.objects.all().delete()

    print("All instruments deleted!")
