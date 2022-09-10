from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "inventory"

urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile"),
    # Django Auth
    path(
        "login",
        auth_views.LoginView.as_view(template_name="inventory/login.html"),
        name="login",
    ),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.index, name="index"),
    path("woodwind_metrics", views.woodwind_metrics, name="woodwind_metrics"),
    path("brass_metrics", views.brass_metrics, name="brass_metrics"),
    path("add_instrument", views.add_instrument, name="add_instrument"),
    path("<instrument_id>", views.update_instrument, name="update_instrument"),
]
