from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("instrument_inventory_app.apps.public.urls")),
    path("accounts/", include("instrument_inventory_app.apps.accounts.urls")),
]