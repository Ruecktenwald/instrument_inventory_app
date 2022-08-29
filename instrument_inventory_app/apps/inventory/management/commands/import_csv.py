from django.db import models
from instrument_inventory_app.apps.inventory.models import Student
import pandas as pd

data = pd.read_csv (r'instrument_inventory_app/apps/accounts/csv_files/students.csv')


student = pd.DataFrame(data, columns= ['A','B','C'])


for s in student:
        Student.objects.create(first_name= s[0],last_name= s[1], grade = s[2])
