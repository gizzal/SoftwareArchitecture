from django.urls import path
from django.contrib import admin

from web_app.views.mission import MissionListView, MissionDetailView
from web_app.views.planning import PlanningView
from web_app.views.report import ReportView, generate_report
from web_app.views.vehicle import VehicleView
from web_app.views.prognosis import  FinishedMissionView

urlpatterns = [
    path('', MissionListView.as_view(), name='mission_list'),
    path('mission/<int:pk>', MissionDetailView.as_view(), name='mission'),
    path('mission/<int:pk>/report', ReportView.as_view(), name='report'),
    path('vehicle/<int:pk>', VehicleView.as_view(), name='vehicle'),
    path('report/<int:pk>', generate_report, name='mission_report'),
    path('finished/<int:pk>', FinishedMissionView.as_view(), name='finished'),
    path('planning/<int:pk>', PlanningView.as_view(), name='planning'),
]

admin.site.site_header = 'Optimus - Admin'
