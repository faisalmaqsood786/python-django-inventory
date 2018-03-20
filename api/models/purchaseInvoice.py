from django.db import models
from api.models.vendors import vendors

class purchaseInvoive(models.Model):
    date = models.DateField(max_length=30, blank=False)
    vendor = models.ForeignKey(vendors,on_delete=models.CASCADE, blank=False)
    totalAmount = models.DecimalField(
        blank=True, max_digits=8, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "purchase_inovice"

    def __str__(self):
        return self.date
