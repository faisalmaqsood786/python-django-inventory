from django.db import models
from api.models.employees import employees
from api.models.items import items

class issueInvoice(models.Model):
    date = models.DateField(max_length=30, blank=False)
    employee = models.ForeignKey(employees,on_delete=models.CASCADE, blank=False)
    item = models.ForeignKey(items,on_delete=models.CASCADE, blank=False)
    qty = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "issue_inovice"

    def __str__(self):
        return self.employee.name
