from rest_framework.viewsets import ModelViewSet
from ..models import Month
from .serializers import MonthSerializer
from .permissions import IsAdminOrReadOnly


class MonthApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = MonthSerializer

    queryset = Month.objects.all()
    lookup_field = "id"
