from api.models.users_jwt import users_jwt
from rest_framework import serializers


class userJWT(serializers.ModelSerializer):

    class Meta:
        model = users_jwt
        fields = ['jwt', 'user']
