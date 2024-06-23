from django.urls import path, include
from . import views



urlpatterns = [
    path("api/", include("users.api.urls")),
    path("login/", views.indexView, name="authentication"),
]
