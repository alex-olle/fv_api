from rest_framework.viewsets import ModelViewSet
from ..models import Fruit
from .serializers import FruitSerializer


class FruitApiViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = FruitSerializer

    queryset = Fruit.objects.all()
    lookup_field = "name"
