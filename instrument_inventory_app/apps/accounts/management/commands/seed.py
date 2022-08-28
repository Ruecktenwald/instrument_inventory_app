# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand

import logging
from django_seed import Seed


seeder = Seed.seeder()

from instrument_inventory_app.apps.accounts.models.py import Locker

seeder.add_entity(Game, 5)
seeder.add_entity(Player, 10)

inserted_pks = seeder.execute()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = "refresh"

""" Clear all data and do not create any object """
MODE_CLEAR = "clear"


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete instances")
    Locker.objects.all().delete()


def create_locker():
    """Creates an address object combining different elements from the list"""
    logger.info("Creating locker")

    locker = Locker(locker_number=self.id)
    locker.save()
    logger.info("{} address created.".format(address))
    return locker


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 addresses
    for i in range(200):
        create_locker()
