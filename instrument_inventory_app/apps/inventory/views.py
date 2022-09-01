from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from instrument_inventory_app.apps.inventory.models import Instrument
from instrument_inventory_app.apps.inventory.forms import InstrumentForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/profile.html"



def instrument(request,instrument_id):
    instrument = Instrument.objects.get(pk=instrument_id)

    return render(request,'instrument.html',
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
        request, "add_instrument.html", {"form" :form, "submitted" :submitted}
    )


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "instruments": Instrument.objects.all().order_by("instrument_kind"),
        # "accessories": Instrument.objects.filter(__endswith="accessory"),
    }
    return render(request, "index.html", context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")
