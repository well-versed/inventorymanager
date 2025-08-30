# inventory/api_urls.py
# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CustomerViewSet, SupplierViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
