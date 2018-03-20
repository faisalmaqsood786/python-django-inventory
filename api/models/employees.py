from django.db import models

class employees(models.Model):
    employeeNo = models.IntegerField(blank=False)
    name = models.CharField(max_length=100, blank=False)
    image = models.CharField(max_length=500, blank=True,null=True)
    mobileNo = models.CharField(max_length=200, blank=True, null=True,unique=True)
    isActive = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employees"

    def __str__(self):
        return self.name
