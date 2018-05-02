import random

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import dateutil.parser

from api.mission.serializers import (
    MissionDetailedSerializer, MissionSerializer, MissionPrognosticsSerializer)
from api.vehicle.serializers import VehicleSerializer
from web_app.models import Mission, Vehicle


class MissionAPIView(ListModelMixin, RetrieveModelMixin,
                     viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = MissionDetailedSerializer
        return super(MissionAPIView, self).retrieve(
            request, *args, **kwargs)


class MissionPrognosticsAPIView(RetrieveAPIView):
    """ For Carlos prognostics page.\n
    Response data format: {"data": [{
            "driver_name": "Walter Nosiglia",
            "name": "Mercedez",
            "type":"Truck",
            "position": "Bolivia",
            "maitenance": "20/02/1999",
            "engine_diagnosis": "40",
            "engine_prognosis": "10",
            "fuel_system_diagnosis": "30",
            "fuel_system_prognosis": "10",
            "battery_diagnosis": "47",
            "battery_prognosis": "27",
            "in_mission":"1"
    }]}
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = MissionPrognosticsSerializer
    queryset = Mission.objects.all()

    def retrieve(self, request, *args, **kwargs):
        result = []
        vehicles_available = Vehicle.objects.filter(Q(status='AVAILABLE') | Q(mission_id=self.kwargs['pk'])).all()
        serializer_available = VehicleSerializer(vehicles_available, many=True)
        vehicles = serializer_available.data
        for vehicle in vehicles:
            v_data = {}
            v_data['id'] = vehicle['id']
            v_data['driver_name'] = vehicle.get('driver', '')
            v_data['name'] = vehicle['name']
            v_data['type'] = vehicle.get('type', '')
            v_data['position'] = vehicle['current_location']
            v_data['maitenance'] = dateutil.parser.parse(vehicle['last_maintenance']).strftime('%d/%m/%Y')
            v_data['in_mission'] = 1 if vehicle.get('mission', '') == self.kwargs['pk'] else 0
            subassies = vehicle['subassies']
            for sub in subassies:
                v_data[sub['name'].lower().replace(' ', '_') + '_diagnosis'] = float(sub['health'])
                v_data[sub['name'].lower().replace(' ', '_') + '_prognosis'] = random.randint(0, float(sub['health']))
            result.append(v_data)
        return Response({'data': result})


class MissionChangeVehicleAPIView(viewsets.GenericViewSet):
    renderer_classes = (JSONRenderer,)
    queryset = Mission.objects.all()

    def change(self, request, *args, **kwargs):
        vehicle_id = request.data['id']
        vehicle = Vehicle.objects.get(pk=vehicle_id)

        if vehicle.mission_id != int(kwargs['pk']):
            vehicle.mission_id=kwargs['pk']
        else:
            vehicle.mission_id = None
        vehicle.save()
        return Response({'data': 'ok'})
