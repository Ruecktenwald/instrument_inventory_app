from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from instrument_inventory_app.apps.inventory.models import Instrument
from instrument_inventory_app.apps.inventory.forms import InstrumentForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/profile.html"








def index(request):
    instruments = Instrument.objects.all().order_by("instrument_kind")

    return render(request, "index.html" ,
        {'instruments' : instruments})


def instrument(request,instrument_id):
    instrument = Instrument.objects.get(pk=instrument_id)

    return render(request,'instruments/instrument.html',
    {'instrument' : instrument})



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
        request, "instruments/add_instrument.html", {"form" :form, "submitted" :submitted}
    )


def update_instrument(request, instrument_id):
    instrument = Instrument.objects.get(pk=instrument_id)
    form = InstrumentForm(request.POST or None, instance=instrument)

    if form.is_valid():
        form.save()
        return redirect("inventory:index")

    return render(request,'instruments/update_instrument.html',
    {"form" :form, "instrument" :instrument})










def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")
