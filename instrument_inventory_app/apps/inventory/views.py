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


@login_required(redirect_field_name='index')
def index(request):
    instruments = Instrument.objects.all().order_by("instrument_kind")

    return render(request, "index.html" ,
        {'instruments' : instruments})

@login_required(redirect_field_name='index')
def instrument(request,instrument_id):
    instrument = Instrument.objects.get(pk=instrument_id)

    return render(request,'instrument.html',
    {'instrument' : instrument})


@login_required(redirect_field_name='index')
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

@login_required(redirect_field_name='index')
def update_instrument(request, instrument_id):
    instrument = Instrument.objects.get(pk=instrument_id)
    form = InstrumentForm(request.POST or None, instance=instrument)

    if form.is_valid():
        form.save()
        return redirect("inventory:index")

    return render(request,'update_instrument.html',
    {"form" :form, "instrument" :instrument})



@login_required(redirect_field_name='index')
def metrics(request: HttpRequest) -> HttpResponse:

    instruments = Instrument.objects.all()


    ##########################
    # Woodwind Part Queries  #
    ##########################

    # Count the total amount of Reeds in inventory
    reeds_only = Instrument.objects.filter(reeds_accessory=True).count()

    # Count the total amount of Ligatures in inventory
    ligatures_only = Instrument.objects.filter(ligature_accessory=True).count()

    # Count the total amount of Ligatures in inventory
    woodwind_mouth_piece_accessory_only = Instrument.objects.filter(instrument_kind__in=['clarinet','bass clarinet','oboe','alto sax','tenor sax','baritone sax',
    'bassoon'],mouth_piece_accessory=True).count()



    ############################
    # Brass Mouth Piece Queries#
    ############################

    # Count the total amount of Trumpet Books in inventory

    trumpet_mouth_piece_accessory_only = Instrument.objects.filter(instrument_kind='trumpet', mouth_piece_accessory=True).count()
    trombone_mouth_piece_accessory_only = Instrument.objects.filter(instrument_kind='trombone', mouth_piece_accessory=True).count()
    french_horn_mouth_piece_accessory_only = Instrument.objects.filter(instrument_kind='french horn', mouth_piece_accessory=True).count()
    baritone_horn_mouth_piece_accessory_only = Instrument.objects.filter(instrument_kind='baritone horn', mouth_piece_accessory=True).count()


     ##########################
    # Instrument Book Queries#
    ##########################

    # Count the total amount of alto_sax_books_count Books in inventory
    trumpet_books_only = Instrument.objects.filter(instrument_kind="trumpet",book_accessory=True).count()
    alto_sax_books_only = Instrument.objects.filter(instrument_kind="alto sax",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    clarinet_books_only = Instrument.objects.filter(instrument_kind="clarinet",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    bassoon_books_only = Instrument.objects.filter(instrument_kind="bassoon",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    oboe_books_only = Instrument.objects.filter(instrument_kind="oboe",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    flute_books_only = Instrument.objects.filter(instrument_kind="flute",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    bass_clarinet_books_only = Instrument.objects.filter(instrument_kind="bass clarinet",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    tenor_sax_books_only = Instrument.objects.filter(instrument_kind="tenor sax",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    baritone_sax_books_only = Instrument.objects.filter(instrument_kind="baritone sax",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    french_horn_sax_books_only = Instrument.objects.filter(instrument_kind="french horn",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    trombone_books_only = Instrument.objects.filter(instrument_kind="trombone",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    baritone_horn_books_only = Instrument.objects.filter(instrument_kind="baritone horn",book_accessory=True).count()

     # Count the total amount of alto_sax_books_count Books in inventory
    bass_guitar_books_only = Instrument.objects.filter(instrument_kind="bass guitar",book_accessory=True).count()




    return render(request, "metrics.html",{'baritone_horn_mouth_piece_accessory_only':baritone_horn_mouth_piece_accessory_only,
        'french_horn_mouth_piece_accessory_only':french_horn_mouth_piece_accessory_only,
        'trombone_mouth_piece_accessory_only':trombone_mouth_piece_accessory_only,
        'trumpet_mouth_piece_accessory_only':trumpet_mouth_piece_accessory_only,
        'woodwind_mouth_piece_accessory_only':woodwind_mouth_piece_accessory_only,
        'instruments':instruments,'reeds_only':reeds_only,'ligatures_only':ligatures_only,
        'trumpet_books_only':trumpet_books_only,'alto_sax_books_only':alto_sax_books_only,
        'clarinet_books_only':clarinet_books_only,'bassoon_books_only':bassoon_books_only,'oboe_books_only':oboe_books_only,
        'flute_books_only':flute_books_only, 'bass_clarinet_books_only':bass_clarinet_books_only,
        'tenor_sax_books_only':tenor_sax_books_only,'baritone_sax_books_only':baritone_sax_books_only,
        'french_horn_sax_books_only':french_horn_sax_books_only,'trombone_books_only':trombone_books_only,
        'baritone_horn_books_only':baritone_horn_books_only,'bass_guitar_books_only':bass_guitar_books_only,})




def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")



