from django.contrib import admin
from django.forms import ModelForm

from web_app.models import (
    Mission, VehicleType, Vehicle, SubSystem, Sensor, ConcreteSubSystem,
    MissionPoint, MissionPointSensorsData)


class VehicleAdminForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ('name', 'status', 'type', 'current_location', 'mission', 'driver')


class SubSystemAdminForm(ModelForm):
    class Meta:
        model = SubSystem
        fields = ('name', 'vehicle_type')


class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'subsystem', 'slug', 'obd_code', 'unit', 'lower_bound', 'upper_bound')
    readonly_fields = ('slug',)


class ConcreteSubsystemInline(admin.TabularInline):
    model = ConcreteSubSystem
    extra = 1


class VehicleAdmin(admin.ModelAdmin):
    form = VehicleAdminForm
    list_display = ('name', 'status', 'type', 'current_location', 'mission', 'driver', 'last_maintenance')
    inlines = [ConcreteSubsystemInline, ]


class SubSystemAdmin(admin.ModelAdmin):
    form = SubSystemAdminForm
    list_display = ('name', 'vehicle_type')


class VehicleInline(admin.TabularInline):
    model = Vehicle
    extra = 1


class MissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'departure_point', 'arrival_point', 'started_at', 'ended_at', 'actual_end_at', 'status')
    inlines = [VehicleInline, ]


admin.site.register(Mission, MissionAdmin)
admin.site.register(VehicleType)
admin.site.register(ConcreteSubSystem)
admin.site.register(MissionPoint)
admin.site.register(MissionPointSensorsData)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(SubSystem, SubSystemAdmin)
admin.site.register(Sensor, SensorAdmin)
