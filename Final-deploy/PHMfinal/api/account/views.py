from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from web_app.models import Vehicle, Sensor
from account.models import Config
from api.account.serializers import GetAllSerializer, ConfigSerializer


class LoginViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    Authorize user via API
    """
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


class GetAllAPIView(APIView):
    """
    Get all information for user signed-in in Android application.
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)

    """
    Get all information for user signed-in in Android application.
    """

    def get(self, request, format=None):
        user = request.user
        vehicle = Vehicle.objects.filter(driver__user=user).first()
        if not vehicle:
            return Response({
                'error': {
                    'msg': 'No data associated for current user. Please contact your supervision operator.'
                }
            }, 400)

        mission = vehicle.mission
        sensors = Sensor.objects.all()

        return Response(GetAllSerializer({
            'mission': mission,
            'vehicle': vehicle,
            'sensors': sensors,
        }).data)


class GetConfigAPIView(APIView):
    """ Get configuration data of the service """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        config = Config.objects.all().first()
        if not config:
            return Response({
                'error': {
                    'msg': 'No config exists.'
                }
            }, 400)

        return Response(ConfigSerializer(config).data)
