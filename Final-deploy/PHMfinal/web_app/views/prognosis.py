# coding: utf-8
from django.views.generic import DetailView

from web_app.models import Vehicle, Mission


class FinishedMissionView(DetailView):
    template_name = "finished_mission.html"
    model = Mission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['vehicle_list'] = Vehicle.objects.filter(
            mission=self.kwargs['pk']).select_related('type')

        return context


class MissionDetailView(DetailView):
    template_name = "mission.html"
    model = Mission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['vehicle_list'] = Vehicle.objects.filter(mission=self.kwargs['pk']).select_related('type')

        return context