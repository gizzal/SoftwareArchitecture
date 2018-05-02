from django.contrib import admin

# Register your models here.
from supervision.models import OperationalCostSpareParts, OperationalCostWorkload


class OperationalCostSparePartsAdmin(admin.ModelAdmin):
    model = OperationalCostSpareParts
    list_display = ('created_at', 'amount')


class OperationalCostWorkloadAdmin(admin.ModelAdmin):
    model = OperationalCostWorkload
    list_display = ('created_at', 'amount')


admin.site.register(OperationalCostSpareParts, OperationalCostSparePartsAdmin)
admin.site.register(OperationalCostWorkload, OperationalCostWorkloadAdmin)
