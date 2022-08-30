from django.contrib import admin

from .models import Instrument, InstrumentKind, Locker, Student

admin.site.register(Instrument)
admin.site.register(Locker)
admin.site.register(Student)
