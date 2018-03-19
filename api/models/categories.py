from django.db import models

class categories(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.CharField(max_length=500, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name
