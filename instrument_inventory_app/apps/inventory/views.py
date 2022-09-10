from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from instrument_inventory_app.apps.inventory.models import Instrument
from instrument_inventory_app.apps.inventory.forms import InstrumentForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/profile.html"


@login_required(redirect_field_name="index")
def index(request):
    instruments = Instrument.objects.all().order_by("instrument_kind")

    return render(request, "index.html", {"instruments": instruments})


@login_required(redirect_field_name="index")
def instrument(request, instrument_id):
    instrument = Instrument.objects.get(pk=instrument_id)

    return render(request, "instrument.html", {"instrument": instrument})


@login_required(redirect_field_name="index")
def add_instrument(request):
    submitted = False
    if request.method == "POST":
        form = InstrumentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("add_instrument?submitted=True")
    else:
        form = InstrumentForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "add_instrument.html", {"form": form, "submitted": submitted}
    )


@login_required(redirect_field_name="index")
def update_instrument(request, instrument_id):
    instrument = Instrument.objects.get(pk=instrument_id)
    form = InstrumentForm(request.POST or None, instance=instrument)

    if form.is_valid():
        form.save()
        return redirect("inventory:index")

    return render(
        request, "update_instrument.html", {"form": form, "instrument": instrument}
    )


#############################################################################
# INSTRUMENT Queries
#############################################################################


@login_required(redirect_field_name="index")
def brass_metrics(request: HttpRequest) -> HttpResponse:

    instruments = Instrument.objects.filter(
        instrument_kind__in=["trumpet", "trombone", "french horn", "baritone horn"]
    )
    instruments_with_missing_items = []

    
    ############################
    # Brass Instrument Queries#
    ############################

    for instrument in instruments:
        if (
            instrument.polishing_cloth_accessory == False
            or instrument.oil_accessory == False
            or instrument.mouth_piece_accessory == False
            or instrument.book_accessory == False
        ):
            instruments_with_missing_items.append(instrument)



    return render(
        request,
        "brass_metrics.html",
        {
            "instruments_with_missing_items": instruments_with_missing_items,
            "instruments": instruments,
        },
    )


@login_required(redirect_field_name="index")
def woodwind_metrics(request: HttpRequest) -> HttpResponse:

    instruments = Instrument.objects.filter(
        instrument_kind__in=["alto sax", "tenor sax", "baritone sax", "oboe", "bassoon"]
    )

   
    instruments_with_missing_items = []


    ##########################
    # Woodwind Part Queries  #
    ##########################
  

    for instrument in instruments:
        if (
            instrument.swab_accessory == False
            or instrument.reeds_accessory == False
            or instrument.mouth_piece_accessory == False
            or instrument.book_accessory == False
            or instrument.ligature_accessory == False
            or instrument.cork_grease_accessory == False
            
        ):
            instruments_with_missing_items.append(instrument)


    return render(
        request,
        "woodwind_metrics.html",
        {
            "instruments_with_missing_items": instruments_with_missing_items,
            "instruments": instruments,
        },
    )
  



