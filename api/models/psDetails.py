from django.db import models
from api.models.purchaseInvoice import purchaseInvoive
from api.models.items import items

class psDetails(models.Model):
    master_id = models.DateField(purchaseInvoive,blank=False)
    item = models.ForeignKey(items, blank=False)
    totalAmount = models.DecimalField(
        blank=True, max_digits=8, decimal_places=2, null=True)
    qty = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ps_invoice_details"

    def __str__(self):
        return self.master_id
