from django.db import models
from instrument_inventory_app.apps.accounts.models import Locker

Locker.objects.all().delete()

print("200 lockers deleted!")
