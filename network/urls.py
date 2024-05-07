from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, ProductViewSet, MyTokenObtainPairView, SupplierFilterView
from . import views

# Создаем маршрутизатор и регистрируем наше представление
router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('filter/', SupplierFilterView.as_view(), name='filter_country'),
]
