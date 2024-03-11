from rest_framework import serializers
from ..models import Month


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = ["id", "name", "slug", "number"]
