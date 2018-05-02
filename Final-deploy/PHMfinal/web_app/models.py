import math
from datetime import date

from django.db import models
from autoslug import AutoSlugField

from account.models import Profile


#  depricated (maybe???)
class Environment(models.Model):
    # id uuid NOT NULL,
    name = models.CharField(max_length=200)
    time = models.BigIntegerField()
    value = models.BigIntegerField()

    class Meta:
        db_table = "env"


# depricated (maybe???)
class System(models.Model):
    # id uuid NOT NULL,
    name = models.CharField(max_length=200)
    time = models.BigIntegerField()
    value = models.BigIntegerField()

    class Meta:
        db_table = "sys"


class SubSystem(models.Model):
    """ Subassy type, element of a vehicle_type. Example: battery, engine, braking system """
    name = models.CharField(max_length=200)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "sub_sys"

    def __str__(self):
        return self.name


class ConcreteSubSystem(models.Model):
    """ Concrete subassy of a concrete vehicle """
    subsystem = models.ForeignKey('SubSystem', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', related_name='subassies', on_delete=models.CASCADE)
    health = models.DecimalField('Current Health', max_digits=5, decimal_places=1)

    class Meta:
        db_table = "concrete_sub_sys"

    def __str__(self):
        return '{} - {}'.format(self.vehicle.name, self.subsystem.name)


class Sensor(models.Model):
    """ Example: Speed, Calculated engine load, Intake air temperature, Throttle position """
    subsystem = models.ForeignKey(SubSystem, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', always_update=True, unique=True, null=True)
    obd_code = models.CharField(max_length=50, null=True, blank=True)
    unit = models.CharField('Unit of Measurement', max_length=50, null=True, blank=True)
    lower_bound = models.DecimalField('Lower bound of warning threshold', max_digits=9, decimal_places=6, default=0.0)
    upper_bound = models.DecimalField('Upper bound of warning threshold', max_digits=9, decimal_places=6, default=100.0)

    class Meta:
        db_table = "sensor"

    def __str__(self):
        return self.name


class Mission(models.Model):
    """ Transport mission to deliver a cargo from one point to another """
    # todo: move Points to separate entity
    departure_point = models.CharField(max_length=200)
    arrival_point = models.CharField(max_length=200)
    departure_long = models.DecimalField('Departure Longitude', max_digits=9, decimal_places=6, null=True, blank=True)
    departure_lat = models.DecimalField('Departure Latitude', max_digits=9, decimal_places=6, null=True, blank=True)
    arrival_long = models.DecimalField('Arrival Longitude', max_digits=9, decimal_places=6, null=True, blank=True)
    arrival_lat = models.DecimalField('Arrival Latitude', max_digits=9, decimal_places=6, null=True, blank=True)
    started_at = models.DateTimeField('Planned Start Time', null=True, blank=True)
    ended_at = models.DateTimeField('Planned Finish Time', null=True, blank=True)
    actual_end_at = models.DateTimeField('Actual Finish Time', null=True, blank=True)

    class Meta:
        db_table = "mission"

    def __str__(self):
        return self.name

    @property
    def status(self):
        if self.ended_at and (date.today() > self.ended_at.date()):
            return 'Finished'
        elif self.started_at and (date.today() < self.started_at.date()):
            return 'Planned'
        else:
            return 'Active'

    @property
    def name(self):
        return '{} - {}'.format(self.departure_point, self.arrival_point)

    @property
    def distance(self):
        a = round(
            math.sqrt(
                ((self.arrival_lat - self.departure_lat) * (self.arrival_lat - self.departure_lat)) +
                ((self.arrival_long - self.departure_long) * (self.arrival_long - self.departure_long))
            )
            , 2)

        return a * 12.5

    @property
    def delay_abs(self):
        """ Mission delay in hours. """
        if self.ended_at and self.actual_end_at:
            delta = self.actual_end_at - self.ended_at
            hours, remainder = divmod(delta.seconds, 3600)
            hours = delta.days * 24 + hours
            return hours
        else:
            return None

    @property
    def delay_percentage(self):
        """ Mission delay in percents. """
        if self.delay_abs and self.started_at:
            planned_delta = self.ended_at - self.started_at
            planned_hours, remainder = divmod(planned_delta.seconds, 3600)
            print(planned_hours, remainder)
            delay_percentage = self.delay_abs / (planned_delta.days * 24 + planned_hours) * 100
            return round(delay_percentage, 1)
        else:
            return None


class VehicleType(models.Model):
    """ Vehicle type (truck, four-wheeler) """
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "vehicle_type"

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    """ Concrete vehicle """
    AVAILABLE = 'AVAILABLE'
    MAINTENANCE = 'MAINTENANCE'
    RESERVED = 'RESERVED'
    MISSION = 'MISSION'
    STATUSES = (
        (AVAILABLE, 'Available'),
        (MAINTENANCE, 'In maintenance'),
        (RESERVED, 'Reserved for mission'),
        (MISSION, 'In mission'),
    )
    status = models.CharField(max_length=100, choices=STATUSES, default=AVAILABLE)
    mission = models.ForeignKey(Mission, related_name='vehicles', on_delete=models.CASCADE, null=True, blank=True)
    driver = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    type = models.ForeignKey(VehicleType, verbose_name='Vehicle Type', on_delete=models.CASCADE, null=True)
    current_location = models.CharField(max_length=200, default='Main Station')
    last_maintenance = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = "vehicle"

    def __str__(self):
        return self.name

    @property
    def last_mission_point(self):
        return self.missionpoint_set.order_by('timestamp').first()


# depricated
class SensorsData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    time = models.BigIntegerField()
    value = models.BigIntegerField()

    class Meta:
        db_table = "sensors_data"


class MissionPoint(models.Model):
    timestamp = models.BigIntegerField()
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    long = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    alt = models.BigIntegerField()

    class Meta:
        db_table = "mission_point"

    @property
    def warning_sensor_list(self):
        return ', '.join(self.missionpointsensorsdata_set.filter(
            warning=True).values_list('slug', flat=True))

class MissionPointSensorsData(models.Model):
    mission_point = models.ForeignKey(MissionPoint, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, default='')
    warning = models.BooleanField(default=False)
    value = models.CharField(max_length=255, default='')

    class Meta:
        db_table = "mission_point_sensors_data"
