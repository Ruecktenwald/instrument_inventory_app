from django.contrib import admin

from .models import Instrument, InstrumentCategory, Locker, Student

admin.site.register(Instrument)
admin.site.register(InstrumentCategory)
admin.site.register(Locker)
admin.site.register(Student)
