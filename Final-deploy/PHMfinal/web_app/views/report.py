# coding: utf-8
import os
from docxtpl import DocxTemplate
from django.http.response import HttpResponse
from django.views.generic import ListView

from web_app.models import Vehicle, Mission


class ReportView(ListView):
    template_name = "report.html"
    model = Mission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object'] = Mission.objects.get(pk=self.kwargs['pk'])

        context['object_list'] = Vehicle.objects.filter(
            mission=self.kwargs['pk']
        ).select_related('type')

        return context


def generate_report(request, pk):
    path = os.path.join(os.path.abspath(os.path.curdir), "report.docx")
    doc = DocxTemplate(path)

    mission = Mission.objects.get(id=pk)

    vehicles = Vehicle.objects.filter(
        mission=pk
    ).select_related('type')

    for i, veh in enumerate(vehicles):
        veh.distance = mission.distance
        veh.average_speed = 70 if i == 0 else 74
        veh.fuel = 240.3 if i == 0 else 300.7

    result = {'mission_name': mission.name,
              'arrival_point': mission.arrival_point,
              'departure_point': mission.departure_point,
              'started_at': mission.started_at.date(),
              'ended_at': mission.ended_at.date(),
              'vehicle': vehicles,
              }

    doc.render(result)
    doc.save("generated_doc.docx")
    with open("generated_doc.docx", 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/msword")
        response['Content-Disposition'] = 'inline; filename=generated_doc.docx'
        return response
