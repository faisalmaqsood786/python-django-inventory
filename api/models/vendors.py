from django.db import models

class vendors(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.CharField(max_length=500, blank=True,null=True)
    mobileNo = models.CharField(max_length=200, blank=True, null=True,unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    isActive = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vendors"

    def __str__(self):
        return self.name
