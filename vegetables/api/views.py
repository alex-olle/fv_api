from rest_framework.viewsets import ModelViewSet
from ..models import Vegetable
from .permissions import IsAdminOrReadOnly
from .serializers import VegetableSerializer


class VegetableApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = VegetableSerializer

    queryset = Vegetable.objects.all()
    lookup_field = "id"
