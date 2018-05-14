from rest_framework import serializers
from api.models.categories import categories
from api.models.items import items
from api.models.vendors import vendors
from api.models.categories import categories


class GetCategory(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = ['name']

class GetVendor(serializers.ModelSerializer):
    class Meta:
        model = vendors
        exclude = ['name','mobileNo','address']

class ProductSerializer(serializers.ModelSerializer):
    category = GetCategory(read_only=True)
    vendor = GetVendor(read_only=True)
    # booking_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = items
        exclude = []
