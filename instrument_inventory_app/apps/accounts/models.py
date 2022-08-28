from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from enum import Enum
from django_seed import Seed


class Locker(models.Model):
    locker_number = models.CharField(max_length=3, unique=True, blank=True, null=True)

    # LOCKERS.append(locker_number)

    def __str__(self):
        return self.locker_number


class Student(models.Model):
    class Grades(Enum):  # A subclass of Enum

        fifth = "5"
        sixth = "6"
        seventh = "7"
        eighth = "8"

    class Homeroom(Enum):  # A subclass of Enum

        o = "O"
        g = "G"
        p = "P"
        s = "S"

    student_first_name = models.CharField(
        max_length=64, unique=True, blank=True, null=True
    )
    student_last_name = models.CharField(
        max_length=64, unique=True, blank=True, null=True
    )

    grade = models.CharField(
        max_length=10, choices=[(tag.name, tag.value) for tag in Grades]
    )
    homeroom = models.CharField(
        max_length=10, choices=[(tag.name, tag.value) for tag in Homeroom]
    )

    def __str__(self):
        return self.student_first_name + " " + self.student_last_name


class InstrumentCategory(models.Model):
    class classification(DjangoChoices):
        woodwind_instrument = ChoiceItem()
        reed_instrument = ChoiceItem()
        brass_instrument = ChoiceItem()
        percussion_instrument = ChoiceItem()

    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(
        max_length=64,
        choices=classification.choices,
    )

    def __str__(self):
        return self.name


class InstrumentCondition(DjangoChoices):
    broken = ChoiceItem()
    needs_repair_soon = ChoiceItem()
    decent_condition = ChoiceItem()
    excellent_condition = ChoiceItem()
    in_repair_shop = ChoiceItem()


class Instrument(models.Model):

    locker_number = models.OneToOneField(
        Locker, on_delete=models.SET_NULL, blank=True, null=True
    )  # details

    student = models.OneToOneField(
        Student, on_delete=models.SET_NULL, blank=True, null=True
    )  # details

    instrument_name = models.CharField(max_length=64, blank=True, null=True)
    serial_number = models.CharField(max_length=64, unique=True, blank=True, null=True)

    condition = models.CharField(
        max_length=64, choices=InstrumentCondition.choices, blank=True, null=True
    )

    # Woodwind/Reed items
    mouth_piece = models.BooleanField(default=True)
    ligature = models.BooleanField(default=True)
    cork_grease = models.BooleanField(default=True)
    reeds = models.BooleanField(default=True)
    case = models.BooleanField(default=True)

    notes = models.CharField(max_length=500, blank=True, null=True)

    instrument_category = models.ForeignKey(
        InstrumentCategory, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return (
            self.instrument_name
            + " - Serial#: "
            + self.serial_number
            + " - Locker#: "
            + self.locker_number.locker_number
        )
