from rest_framework.viewsets import ModelViewSet
from ..models import Fruit
from .permissions import IsAdminOrReadOnly
from .serializers import FruitSerializer


class FruitApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = FruitSerializer

    queryset = Fruit.objects.all()
    lookup_field = "id"
