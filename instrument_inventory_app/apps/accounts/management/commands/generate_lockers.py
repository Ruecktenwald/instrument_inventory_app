from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.accounts.models import Locker


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    for i in range(1, 200):
        Locker.objects.create(locker_number=i)

    print("200 lockers created!")

    def handle(self, *args, **kwargs):
        pass
