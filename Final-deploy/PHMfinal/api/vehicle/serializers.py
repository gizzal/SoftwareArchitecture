from rest_framework import serializers

from web_app.models import Vehicle, ConcreteSubSystem


class ConcreteSubSystemSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='subsystem.name')

    class Meta:
        model = ConcreteSubSystem
        fields = ('id', 'health', 'name')


class VehicleSerializer(serializers.ModelSerializer):
    subassies = ConcreteSubSystemSerializer(many=True, read_only=True)
    type = serializers.ReadOnlyField(source='type.name')
    driver = serializers.ReadOnlyField(source='driver.fullname')

    class Meta:
        model = Vehicle
        fields = '__all__'
