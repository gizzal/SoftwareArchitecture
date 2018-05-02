from collections import defaultdict

import django_filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from api.vehicle.serializers import VehicleSerializer
from web_app.models import Vehicle


class VehicleAPIView(ListAPIView):
    """ 
    Get list of vehicles for a mission, driver, type (optional)\n
    http://example.com/api/vehicle?mission=1
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('mission', 'driver', 'type')
