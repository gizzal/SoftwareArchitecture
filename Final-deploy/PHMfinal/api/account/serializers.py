from rest_framework import serializers

from django.contrib.auth import authenticate, login

from web_app.models import Mission, Vehicle, Sensor
from account.models import Config


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(self.context['request'], user)
            return data
        else:
            raise serializers.ValidationError('Username or Password is wrong.')

    def create(self, data):
        return True


class SensorsDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'unit', 'obd_code', 'slug', 'lower_bound', 'upper_bound')


class VehicleDetailedSerializer(serializers.ModelSerializer):
    type = serializers.ReadOnlyField(source='type.name')

    class Meta:
        model = Vehicle
        fields = ('id', 'name', 'type')


class MissionDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('id', 'departure_point', 'arrival_point', 'departure_long',
                  'departure_lat', 'arrival_long', 'arrival_lat', 'started_at',
                  'ended_at')


class GetAllSerializer(serializers.Serializer):
    mission = MissionDetailedSerializer()
    vehicle = VehicleDetailedSerializer()
    sensors = SensorsDetailedSerializer(many=True)


class ConfigSerializer(serializers.ModelSerializer):
    """ Configuration data of the service """
    class Meta:
        model = Config
        fields = ('broker_ip', 'broker_http_port', 'broker_ws_port')
