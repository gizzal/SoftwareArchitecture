# coding: utf-8
from django.views.generic import DetailView

from web_app.models import Vehicle, Mission


class VehicleView(DetailView):
    template_name = "vehicle.html"
    model = Vehicle
