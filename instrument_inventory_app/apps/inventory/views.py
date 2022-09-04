from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from instrument_inventory_app.apps.inventory.models import Instrument
from instrument_inventory_app.apps.inventory.forms import InstrumentForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


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
def brass_metrics(request: HttpRequest) -> HttpResponse:

    instruments = Instrument.objects.filter(instrument_kind__in=['trumpet','trombone','french horn','baritone horn'])
    missing_oil_or_cloth = []

    brass_instruments_kind = ['trumpets', 'trombone','french_horn', 'baritone_horn']
    brass_instruments_oil = ['trumpet_oil_accessory_only', 'trombone_oil_accessory_only','french_horn_oil_accessory_only', 'baritone_horn_oil_accessory_only']


    instruments_brass = ['trumpet', 'trombone', 'french horn', 'baritone horn']
    instrument_counts = {
    instrument: instruments.filter(instrument_kind=instrument) for instrument in instruments
    }


    brass_count = Sum(instrument_counts.values())









    for instrument in instruments:
        if (instrument.polishing_cloth_accessory == False or
            instrument.oil_accessory == False or
            instrument.mouth_piece_accessory == False or
            instrument.book_accessory == False):
            missing_oil_or_cloth.append(instrument)



    ############################
    # Brass Instrument Queries#
    ############################


    trumpet_only = instruments.filter(instrument_kind='trumpet').count()
    trombone_only = instruments.filter(instrument_kind='trombone').count()
    french_horn_only = instruments.filter(instrument_kind='french horn').count()
    baritone_horn_only = instruments.filter(instrument_kind='baritone horn').count()


    trumpet_oil_accessory_only = instruments.filter(instrument_kind='trumpet', oil_accessory=True).count()
    trombone_oil_accessory_only = instruments.filter(instrument_kind='trombone', oil_accessory=True).count()
    french_horn_oil_accessory_only = instruments.filter(instrument_kind='french horn', oil_accessory=True).count()
    baritone_horn_oil_accessory_only = instruments.filter(instrument_kind='baritone horn', oil_accessory=True).count()


    trumpet_mouth_piece_accessory_only = instruments.filter(instrument_kind='trumpet', mouth_piece_accessory=True).count()
    trombone_mouth_piece_accessory_only = instruments.filter(instrument_kind='trombone', mouth_piece_accessory=True).count()
    french_horn_mouth_piece_accessory_only = instruments.filter(instrument_kind='french horn', mouth_piece_accessory=True).count()
    baritone_horn_mouth_piece_accessory_only = instruments.filter(instrument_kind='baritone horn', mouth_piece_accessory=True).count()

    trumpet_polishing_cloth_accessory_only = instruments.filter(instrument_kind='trumpet', polishing_cloth_accessory=True).count()
    trombone_polishing_cloth_accessory_only = instruments.filter(instrument_kind='trombone', polishing_cloth_accessory=True).count()
    french_horn_polishing_cloth_accessory_only = instruments.filter(instrument_kind='french horn', polishing_cloth_accessory=True).count()
    baritone_horn_polishing_cloth_accessory_only = instruments.filter(instrument_kind='baritone horn', polishing_cloth_accessory=True).count()

    total_brass = trumpet_only + trombone_only + french_horn_only + baritone_horn_only
    total_polishing_cloths = trumpet_polishing_cloth_accessory_only + trombone_polishing_cloth_accessory_only + french_horn_polishing_cloth_accessory_only + baritone_horn_polishing_cloth_accessory_only
    total_oil = trumpet_oil_accessory_only + trombone_oil_accessory_only + french_horn_oil_accessory_only + baritone_horn_oil_accessory_only

    trumpet_books_only = Instrument.objects.filter(instrument_kind="trumpet",book_accessory=True).count()
    french_horn_sax_books_only = Instrument.objects.filter(instrument_kind="french horn",book_accessory=True).count()
    trombone_books_only = Instrument.objects.filter(instrument_kind="trombone",book_accessory=True).count()
    baritone_horn_books_only = Instrument.objects.filter(instrument_kind="baritone horn",book_accessory=True).count()
     # Count the total amount of alto_sax_books_count Books in inventory






     # Count the total amount of alto_sax_books_count Books in inventory



    return render(request, "brass_metrics.html",{'instrument_counts':instrument_counts,'brass_count':brass_count,'brass_instruments_oil':brass_instruments_oil,'brass_instruments_kind':brass_instruments_kind,'missing_oil_or_cloth':missing_oil_or_cloth,'french_horn_only':french_horn_only,'baritone_horn_only':baritone_horn_only,
        'trumpet_only':trumpet_only,'trombone_only':trombone_only,'baritone_horn_mouth_piece_accessory_only':baritone_horn_mouth_piece_accessory_only,
        'french_horn_mouth_piece_accessory_only':french_horn_mouth_piece_accessory_only,
        'trombone_mouth_piece_accessory_only':trombone_mouth_piece_accessory_only,
        'trumpet_mouth_piece_accessory_only':trumpet_mouth_piece_accessory_only,
        'instruments':instruments,'trumpet_books_only':trumpet_books_only,'trombone_books_only':trombone_books_only,
        'baritone_horn_books_only':baritone_horn_books_only,
        'trumpet_oil_accessory_only':trumpet_oil_accessory_only,'trombone_oil_accessory_only':trombone_oil_accessory_only,
        'french_horn_oil_accessory_only':french_horn_oil_accessory_only,'baritone_horn_oil_accessory_only':baritone_horn_oil_accessory_only,
        'trumpet_polishing_cloth_accessory_only':trumpet_polishing_cloth_accessory_only,
        'trombone_polishing_cloth_accessory_only':trombone_polishing_cloth_accessory_only,
        'french_horn_polishing_cloth_accessory_only':french_horn_polishing_cloth_accessory_only,
        'baritone_horn_polishing_cloth_accessory_only':baritone_horn_polishing_cloth_accessory_only,
        'total_brass':total_brass,'total_polishing_cloths':total_polishing_cloths,'total_oil':total_oil,


        })








@login_required(redirect_field_name='index')
def woodwind_metrics(request: HttpRequest) -> HttpResponse:

    instruments = Instrument.objects.filter(instrument_kind__in=['alto sax','tenor sax','baritone sax','oboe','bassoon'])


    ##########################
    # Woodwind Part Queries  #
    ##########################




# 'woodwind_mouth_piece_accessory_only':woodwind_mouth_piece_accessory_only,
# 'reeds_only':reeds_only,'ligatures_only':ligatures_only,'clarinet_books_only':clarinet_books_only,
# 'bassoon_books_only':bassoon_books_only,'oboe_books_only':oboe_books_only,
#         'flute_books_only':flute_books_only, 'bass_clarinet_books_only':bass_clarinet_books_only,
#         'tenor_sax_books_only':tenor_sax_books_only,'baritone_sax_books_only':baritone_sax_books_only,


    return render(request, "woodwind_metrics.html",{})



    # 'bass_guitar_books_only':bass_guitar_books_only,
# 'alto_sax_books_only':alto_sax_books_only,
#         'french_horn_sax_books_only':french_horn_sax_books_only,

    # bass_guitar_books_only = Instrument.objects.filter(instrument_kind="bass guitar",book_accessory=True).count()


    # alto_sax_books_only = Instrument.objects.filter(instrument_kind="alto sax",book_accessory=True).count()

    #  # Count the total amount of alto_sax_books_count Books in inventory
    # clarinet_books_only = Instrument.objects.filter(instrument_kind="clarinet",book_accessory=True).count()

    #  # Count the total amount of alto_sax_books_count Books in inventory
    # bassoon_books_only = Instrument.objects.filter(instrument_kind="bassoon",book_accessory=True).count()

    #  # Count the total amount of alto_sax_books_count Books in inventory
    # oboe_books_only = Instrument.objects.filter(instrument_kind="oboe",book_accessory=True).count()

    #  # Count the total amount of alto_sax_books_count Books in inventory
    # flute_books_only = Instrument.objects.filter(instrument_kind="flute",book_accessory=True).count()

    #  # Count the total amount of alto_sax_books_count Books in inventory
    # bass_clarinet_books_only = Instrument.objects.filter(instrument_kind="bass clarinet",book_accessory=True).count()

    #  # Count the total amount of alto_sax_books_count Books in inventory
    # tenor_sax_books_only = Instrument.objects.filter(instrument_kind="tenor sax",book_accessory=True).count()

    #  # Count the total amount of alto_sax_books_count Books in inventory
    # baritone_sax_books_only = Instrument.objects.filter(instrument_kind="baritone sax",book_accessory=True).count()

    #  # Count the total amount of alto_sax_books_count Books in inventory
    #
