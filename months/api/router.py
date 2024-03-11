from rest_framework.routers import DefaultRouter
from .views import MonthApiViewSet

router_months = DefaultRouter()

router_months.register(prefix="month", basename="month", viewset=MonthApiViewSet)
