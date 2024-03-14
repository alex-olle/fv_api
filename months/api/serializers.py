from rest_framework import serializers
from ..models import Month

from fruits.api.serializers import FruitSerializer
from vegetables.api.serializers import VegetableSerializer


class MonthSerializer(serializers.ModelSerializer):
    fruits = FruitSerializer(many=True, read_only=True)
    vegetables = VegetableSerializer(many=True, read_only=True)

    class Meta:
        model = Month
        fields = ["id", "name", "slug", "number", "fruits", "vegetables"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["fruits"] = [fruit["name"] for fruit in representation["fruits"]]
        representation["vegetables"] = [
            vegetable["name"] for vegetable in representation["vegetables"]
        ]
        return representation
