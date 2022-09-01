from django import forms
from django.forms import ModelForm
from instrument_inventory_app.apps.inventory.models import Instrument
from djchoices import DjangoChoices, ChoiceItem

class InstrumentForm(ModelForm):
    class Meta:
        model = Instrument
        fields = "__all__"

        labels = {
        'locker_assignment': '',
        'student':'',
        'instrument_kind':'',
        'instrument_name': '',
        'serial_number': '',
        'condition': '',
        'mouth_piece_accessory': 'Mouth Piece',
        'ligature_accessory': 'Ligature',
        'cork_grease_accessory':'Cork Grease',
        'reeds_accessory': 'Reeds',
        'case_accessory':'Case',
        'oil_accessory': 'Instrument Oil',
        'swab_accessory': 'Cleaning Swab',
        'polishing_cloth_accessory': 'Polishing Cloth',
        'book_accessory':'Music Book',
        }

        widgets= {

        'locker_assignment': forms.Select(attrs={'class':"form-control", 'placeholder':'Assign Locker', 'col':1}),
        'student': forms.Select(attrs={'class':"form-control", 'placeholder':'Student Name', 'col':1}),
        'instrument_kind':forms.Select(attrs={'class':"form-control"}, ),
        'instrument_name': forms.TextInput(attrs={'class':"form-control",'placeholder':'Brand/Model', 'col':1}),
        'serial_number': forms.TextInput(attrs={'class':"form-control",'placeholder':'Serial Number', 'col':1}),
        'condition': forms.Select(attrs={'class':"form-control"}),


        'mouth_piece_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),
        'ligature_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),
        'cork_grease_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),
        'reeds_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),
        'case_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),
        'oil_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),
        'swab_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),
        'polishing_cloth_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),
        'book_accessory': forms.CheckboxInput(attrs={'class':"form-check",}),




        'notes': forms.Textarea(attrs={'class': 'form-control','cols': 150, 'rows':8}),

        }


