from django.contrib.auth.models import User
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from account.models import Profile
from web_app.models import Vehicle, Mission, SubSystem, Sensor, VehicleType


class AccountApiTestCase(APITestCase):

    def setUp(self):
        self.mission = Mission.objects.create(departure_point='Innopolis', arrival_point='Kazan',
                                              departure_long=48.747310, departure_lat=55.751716,
                                              arrival_long=49.066081, arrival_lat=55.830431,
                                              started_at='2018-04-05T12:10:00Z',
                                              ended_at='2018-04-05T13:10:00Z'
                                              )
        self.subsystem = SubSystem.objects.create(name='Brakes')
        self.sensor = Sensor.objects.create(subsystem=self.subsystem, name='Front Left Wheel Temperature', unit='')
        self.user = User.objects.create_user(username='john', email='john@example.com', password='12345')
        self.profile = Profile.objects.create(user=self.user)
        self.vehicle_type = VehicleType.objects.create(name='SUV')
        self.vehicle = Vehicle.objects.create(driver=self.profile, mission=self.mission, name='veh1', type=self.vehicle_type)

    def test_login(self):
        data = {'username': 'john', 'password': '12345'}
        url = reverse_lazy('api-login')
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertNotEquals(response.data['token'], '')


    def test_get_all(self):
        token = Token.objects.create(user=self.user)
        url = reverse_lazy('api-get-all')
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Token {}'.format(token.key))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mission', response.data)
        self.assertIn('vehicle', response.data)
        self.assertIn('sensors', response.data)
        self.assertEqual('SUV', response.data['vehicle']['type'])
