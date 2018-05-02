from rest_framework import serializers

from api.vehicle.serializers import VehicleSerializer
from web_app.models import Mission


class MissionDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('id', 'departure_point', 'arrival_point', 'departure_long',
                  'departure_lat', 'arrival_long', 'arrival_lat', 'started_at',
                  'ended_at')


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('id', 'name')


class MissionPrognosticsSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)

    class Meta:
        model = Mission
        fields = '__all__'
