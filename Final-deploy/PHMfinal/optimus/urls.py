"""optimus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from account.views import login, logout, register
from api.account.views import LoginViewSet, GetAllAPIView, GetConfigAPIView
from api.mission.views import MissionAPIView, MissionPrognosticsAPIView, \
    MissionChangeVehicleAPIView
from api.vehicle.views import VehicleAPIView
from .views import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),

    # REST API
    path('api/login/', LoginViewSet.as_view({'post': 'create'}), name='api-login'),
    path('api/get-all/', GetAllAPIView.as_view(), name='api-get-all'),
    path('api/docs/', schema_view, name='api-docs'),
    path('api/mission/<int:pk>', MissionAPIView.as_view({'get': 'retrieve'}), name='mission-id'),
    path('api/mission/', MissionAPIView.as_view({'get': 'list'}), name='mission-list'),
    path('api/mission/<int:pk>/prognostics', MissionPrognosticsAPIView.as_view(), name='mission-prognostics'),
    path('api/mission/<int:pk>/vehicle', MissionChangeVehicleAPIView.as_view({'post': 'change'}), name='mission-change-vehicle'),
    path('api/vehicle/', VehicleAPIView.as_view(), name='vehicle-list'),
    path('api/config/', GetConfigAPIView.as_view(), name='config'),

    path('supervision/', include("supervision.urls")),
    path('', include("web_app.urls")),
]
