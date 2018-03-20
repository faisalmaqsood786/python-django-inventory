from rest_framework import serializers
from api.models.categories import categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        exclude = []
