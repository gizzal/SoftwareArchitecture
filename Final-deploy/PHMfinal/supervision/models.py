from django.db import models


class OperationalCostSpareParts(models.Model):
    """ Operational costs for spare parts """
    created_at = models.DateField()
    amount = models.DecimalField('Money, $', max_digits=9, decimal_places=6)

    class Meta:
        db_table = "cost_spare_parts"

    def __str__(self):
        return str(self.created_at)


class OperationalCostWorkload(models.Model):
    """ Operational costs for workload """
    created_at = models.DateField()
    amount = models.DecimalField('Working Hours', max_digits=9, decimal_places=6)

    class Meta:
        db_table = "workload_spare_parts"

    def __str__(self):
        return str(self.created_at)
