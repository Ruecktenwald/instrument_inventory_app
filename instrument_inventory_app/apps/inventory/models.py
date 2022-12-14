from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from enum import Enum


class Lock(models.Model):
    lock_serial_number = models.CharField(max_length=7, blank=True, null=True)
    combination_number = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return self.lock_serial_number


class Locker(models.Model):
    locker_number = models.CharField(max_length=3, blank=True, null=True)
    lock_assignment = models.OneToOneField(
        Lock, on_delete=models.SET_NULL, blank=False, null=True
    )

    def __str__(self):
        return self.locker_number


class Student(models.Model):
    class Grades(Enum):  # A subclass of Enum

        five = "5"
        six = "6"
        seven = "7"
        eight = "8"

    class Homeroom(Enum):  # A subclass of Enum

        o = "O"
        g = "G"
        p = "P"
        s = "S"

    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)

    grade = models.CharField(
        max_length=10, choices=[(tag.name, tag.value) for tag in Grades]
    )
    homeroom = models.CharField(
        max_length=10, choices=[(tag.name, tag.value) for tag in Homeroom]
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


class InstrumentKind(DjangoChoices):

    oboe = ChoiceItem()
    flute = ChoiceItem()
    clarinet = ChoiceItem()
    bass_clarinet = ChoiceItem()
    bassoon = ChoiceItem()
    alto_sax = ChoiceItem()
    tenor_sax = ChoiceItem()
    baritone_sax = ChoiceItem()
    trumpet = ChoiceItem()
    french_horn = ChoiceItem()
    trombone = ChoiceItem()
    baritone_horn = ChoiceItem()
    guitar = ChoiceItem()
    percussion = ChoiceItem()
    keyboard = ChoiceItem()


class InstrumentCondition(DjangoChoices):
    broken = ChoiceItem()
    needs_repair_soon = ChoiceItem()
    decent_condition = ChoiceItem()
    excellent_condition = ChoiceItem()
    in_repair_shop = ChoiceItem()


class Instrument(models.Model):

    locker_assignment = models.OneToOneField(
        Locker,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )  # details

    student = models.OneToOneField(
        Student, on_delete=models.SET_NULL, blank=True, null=True
    )  # details

    instrument_kind = models.CharField(
        max_length=64, choices=InstrumentKind.choices, blank=False, null=True
    )

    instrument_name = models.CharField(max_length=64, blank=False, null=True)
    serial_number = models.CharField(max_length=64, unique=True, blank=False, null=True)

    condition = models.CharField(
        max_length=64,
        choices=InstrumentCondition.choices,
        default="decent condition",
        blank=True,
        null=True,
    )

    # Instrument accessory items
    mouth_piece_accessory = models.BooleanField(default=True)
    ligature_accessory = models.BooleanField(default=False)
    cork_grease_accessory = models.BooleanField(default=False)
    reeds_accessory = models.BooleanField(default=False)
    case_accessory = models.BooleanField(default=True)
    oil_accessory = models.BooleanField(default=False)
    swab_accessory = models.BooleanField(default=False)
    polishing_cloth_accessory = models.BooleanField(default=False)
    book_accessory = models.BooleanField(default=True)

    notes = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return (
            self.instrument_name
            + " - Serial#: "
            + self.serial_number
            + " - Type: "
            + self.instrument_kind
        )
