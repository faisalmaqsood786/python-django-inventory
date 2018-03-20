from django.db import models
from api.models.vendors import vendors
from api.models.categories import categories

class items(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True,null=True)
    image = models.CharField(max_length=500, blank=True,null=True)
    qty = models.IntegerField(blank=True, null=True,default=0)
    sku = models.CharField(max_length=200, blank=True, null=True)
    costPrice = models.DecimalField(
        blank=True, max_digits=8, decimal_places=2, null=True)
    totalAmount = models.DecimalField(
        blank=True, max_digits=8, decimal_places=2, null=True)
    category = models.ForeignKey(categories,on_delete=models.CASCADE, blank=False)
    vendor = models.ForeignKey(vendors ,on_delete=models.CASCADE, blank=False)
    isActive = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "items"

    def __str__(self):
        return self.name
