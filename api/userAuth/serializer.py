from rest_framework import serializers
from api.models.users import users
from api.models.vendors import vendors

class vendorAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = ['type', 'username', 'id']

class vendorAdminAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = vendors
        fields = [
            'firstName',
            'lastName',
            'id',
            'role',
            'company',
            'isFirstLogin',
            'currentStep',
            'country'
        ]


