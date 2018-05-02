from datetime import date

from django.views.generic import ListView, DetailView

from supervision.models import (
    OperationalCostSpareParts,
    OperationalCostWorkload)
from web_app.models import (
    Mission, Vehicle, SubSystem, ConcreteSubSystem)


class TimelinessListView(ListView):
    template_name = "timeliness.html"
    model = Mission

    def get_queryset(self):
        return Mission.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        missions = Mission.objects.all()
        context['missions_list'] = missions
        sum = 0
        for item in missions:
            if item.delay_abs:
                sum = sum + item.delay_abs
        context['delay_sum'] = sum
        return context


class EffectivenessListView(ListView):
    template_name = "effectiveness.html"

    def get_queryset(self):
        return OperationalCostSpareParts.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_date = date.today()
        context['current_date'] = current_date
        previous_date = current_date.replace(year=current_date.year - 1)
        context['previous_date'] = previous_date
        current_year_start = date(date.today().year, 1, 1)
        context['current_year_start'] = current_year_start
        previous_year_start = current_year_start.replace(year=current_year_start.year - 1)
        context['previous_year_start'] = previous_year_start

        context['spare_parts_previous'] = OperationalCostSpareParts.objects.filter(
            created_at__range=(previous_year_start, previous_date))
        sum = 0
        for item in context['spare_parts_previous']:
            if item:
                sum = sum + item.amount
        context['spare_parts_previous_sum'] = sum

        context['spare_parts_current'] = OperationalCostSpareParts.objects.filter(
            created_at__range=(current_year_start, current_date))
        sum = 0
        for item in context['spare_parts_current']:
            if item:
                sum = sum + item.amount
        context['spare_parts_current_sum'] = sum

        context['workload_previous'] = OperationalCostWorkload.objects.filter(
            created_at__range=(previous_year_start, previous_date))
        sum = 0
        for item in context['workload_previous']:
            if item:
                sum = sum + item.amount
        context['workload_previous_sum'] = sum

        context['workload_current'] = OperationalCostWorkload.objects.filter(
            created_at__range=(current_year_start, current_date))
        sum = 0
        for item in context['workload_current']:
            if item:
                sum = sum + item.amount
        context['workload_current_sum'] = sum

        return context


class RepairmentDetailView(DetailView):
    template_name = "repairment_detailed.html"
    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subsystems'] = SubSystem.objects.filter(
            vehicle_type=context['vehicle'].type)
        return context


class RepairmentListView(ListView):
    template_name = "repairment.html"
    model = Vehicle


class ProcurementView(ListView):
    template_name = "procurement.html"

    def get_queryset(self):
        return ConcreteSubSystem.objects.order_by('health')
