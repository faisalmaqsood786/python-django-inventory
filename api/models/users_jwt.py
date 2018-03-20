from django.db import models
from api.models.users import users


class users_jwt  (models.Model):

    user = models.ForeignKey(users)
    jwt = models.CharField(max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users_jwt"

    def __str__(self):
        return self.user.username
