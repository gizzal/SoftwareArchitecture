# coding: utf-8
from django.views.generic import DetailView

from web_app.models import Vehicle, Mission


class PlanningView(DetailView):
    template_name = "planning.html"
    model = Mission
