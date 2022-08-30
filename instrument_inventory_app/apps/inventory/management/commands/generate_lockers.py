from django.core.management.base import BaseCommand, CommandError
from django.db import models
from instrument_inventory_app.apps.inventory.models import Locker
from django.db import connection
from django.core.management.color import no_style


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "number_of_lockers",
            type=int,
            help="I will show you how to make lockers like a robot.",
        )

    def handle(self, *args, **kwargs):

        number_of_lockers = kwargs["number_of_lockers"]

        for i in range(number_of_lockers):
            Locker.objects.create(locker_number=(i + 1), id=i + 1)

        print(f"{number_of_lockers} lockers created!")
        return
