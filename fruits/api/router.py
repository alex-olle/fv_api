from rest_framework.routers import DefaultRouter
from .views import FruitApiViewSet

router_fruits = DefaultRouter()
router_fruits.register(prefix="fruit", basename="fruit", viewset=FruitApiViewSet)
