from django.db import models
from api.models.userType import userType

class users (models.Model):

    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=150, blank=False)
    type = models.ForeignKey(userType,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    salt = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username.lower()
