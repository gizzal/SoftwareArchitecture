from django.db import models

from account.models import Profile
from web_app.models import Mission, VehicleType


class Dataset(models.Model):
    """ Features and labels for ML model """
    mission = models.ForeignKey(Mission, related_name='dataset', on_delete=models.CASCADE)
    # Weather features
    wind_speed = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    humidity = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    temperature = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pressure = models.DecimalField(max_digits=11, decimal_places=6, null=True, blank=True)
    # Road features
    highway = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    surface = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    smoothness = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    tracktype = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    incline = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    length = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # Vehicle features
    driver = models.ForeignKey(Profile, related_name='dataset', on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(VehicleType, related_name='dataset', verbose_name='Vehicle Type', on_delete=models.CASCADE)
    engine_state = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    fuel_state = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    battery_state = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # Labels
    engine_delta = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    fuel_delta = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    battery_delta = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        db_table = "dataset"

    def __str__(self):
        return self.mission.name
