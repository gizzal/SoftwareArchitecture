# coding: utf-8
import datetime

from django.views.generic import TemplateView
from prognostics.weather import Weather

class WeatherView(TemplateView):
    template_name = "weather.html"

    def get(self, *args, **kwargs):
        lat = 55.751716
        lon = 48.747310
        today = datetime.date.today()
        
        kwargs['weather'] = Weather.get_weather(lat, lon, today)

        return super().get(*args, **kwargs)
