from django.db import models
from instrument_inventory_app.apps.accounts.models import Locker

for i in range(1, 200):
    Locker.objects.create(locker_number=i)

Print("200 lockers created!")
