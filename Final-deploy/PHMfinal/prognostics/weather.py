import datetime

from django.conf import settings
import pyowm

class Weather():

    @staticmethod
    def get_weather(lat, lon, date):
        if not isinstance(lat, float) and not isinstance(lat, int) or lat < -90.0 or lat > 90.0:
            raise ValueError("Invalid value in lat")
        if not isinstance(lon, float) and not isinstance(lon, int) or lon < -180.0 or lon > 180.0:
            raise ValueError("Invalid value in lon")
        if not isinstance(date, datetime.date):
            raise ValueError("Invalid value in date")

        owm = pyowm.OWM(settings.OWM_API_KEY, config_module='optimus.owm_settings')
         
        if owm.get_subscription_type() == 'free' and date < datetime.date.today():
            raise NotImplementedError("Historical weather data is unavailable for free API subscription")
        if owm.get_subscription_type() == 'free' and date > datetime.date.today() + datetime.timedelta(5):
            raise NotImplementedError("Forecast more than 5 days is unavailable for free API subscription")

        if date == datetime.date.today():
            observation = owm.weather_at_coords(lat, lon)
            weather = observation.get_weather()
        else:
            forecaster = owm.three_hours_forecast_at_coords(lat, lon)
            weather = forecaster.get_weather_at("{} 12:00:00+00".format(date.isoformat()))

        result = {
            'wind_speed': weather.get_wind().get('speed', 0),
            'humidity': weather.get_humidity(),
            'temperature': weather.get_temperature('celsius').get('temp', 4.0),
            'pressure': weather.get_pressure().get('press', 101.3),
        }

        return result
