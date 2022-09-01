from django import forms
from django.forms import ModelForm
from instrument_inventory_app.apps.inventory.models import Instrument


class InstrumentForm(ModelForm):
    class Meta:
        model = Instrument
        fields = "__all__"


        # widgets= {

        #     'locker_assignment: forms.Select(attrs={'class': 'form-control'}),
        #     'student': TextInput(attrs={'cols': 80, 'rows': 20}),
        #     'instrument_kind':forms.Select(attrs={'class': 'form-control'}),,
        #     'instrument_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'condition': forms.Select(attrs={'class': 'form-control'}),

        #     'mouth_piece_accessory': forms.BooleanField(attrs={'class': 'form-control'}),
        #     'ligature_accessory': forms.BooleanField(attrs={'class': 'form-control'}),
        #     'cork_grease_accessory': forms.BooleanField(attrs={'class': 'form-control'}),
        #     'reeds_accessory': forms.BooleanField(attrs={'class': 'form-control'}),
        #     'case_accessory': forms.BooleanField(attrs={'class': 'form-control'}),
        #     'oil_accessory': forms.BooleanField(attrs={'class': 'form-control'}),
        #     'swab_accessory': forms.BooleanField(attrs={'class': 'form-control'}),
        #     'polishing_cloth_accessory': forms.BooleanField(attrs={'class': 'form-control'}),
        #     'book_accessory': forms.BooleanField(attrs={'class': 'form-control'}),

        #     'notes': Textarea(attrs={'cols': 80, 'rows': 20}),

        # }




