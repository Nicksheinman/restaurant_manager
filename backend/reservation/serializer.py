from rest_framework import serializers
from .models import Table

class RestarauntGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table

        fields = [
            "id",
            "name",
            "seats",
            "x",
            "y",
            "is_active",
            "table_type",
        ]