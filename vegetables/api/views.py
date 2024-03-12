from rest_framework.viewsets import ModelViewSet
from ..models import Vegetable
from .serializers import VegetableSerializer


class VegetableApiViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = VegetableSerializer

    queryset = Vegetable.objects.all()
    lookup_field = "name"
