from django.db import models


class userType(models.Model):

    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_types"

    def __str__(self):
        return self.name
