from django.contrib import admin

from .models import Instrument, InstrumentKind, Locker, Student, Lock

admin.site.register(Instrument)
admin.site.register(Locker)
admin.site.register(Lock)
admin.site.register(Student)
