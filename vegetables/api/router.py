from rest_framework.routers import DefaultRouter
from .views import VegetableApiViewSet

router_vegetables = DefaultRouter()
router_vegetables.register(
    prefix="vegetable", basename="vegetable", viewset=VegetableApiViewSet
)
