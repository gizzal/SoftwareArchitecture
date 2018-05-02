from django.urls import path
from django.contrib import admin

from supervision.views import (
    TimelinessListView, EffectivenessListView,
    RepairmentDetailView, RepairmentListView, ProcurementView)

urlpatterns = [
    path('timeliness', TimelinessListView.as_view(), name='timeliness'),
    path('effectiveness', EffectivenessListView.as_view(),
         name='effectiveness'),
    path('repairment/<int:pk>', RepairmentDetailView.as_view(),
         name='repairment_detailed'),
    path('repairment', RepairmentListView.as_view(), name='repairment'),
    path('procurement', ProcurementView.as_view(),
         name='procurement'),
]

admin.site.site_header = 'Optimus - Admin'
