from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("instrument_inventory_app.apps.inventory.urls")),
]
