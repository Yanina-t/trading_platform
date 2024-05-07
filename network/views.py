from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Suppliers, Product
from .permissions import IsActiveUserPermission
from .serializers import SupplierSerializer, ProductSerializer, MyTokenObtainPairSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUserPermission]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [SearchFilter]
    search_fields = ['country']  # Фильтрация по полю 'country'
    permission_classes = [IsAuthenticated, IsActiveUserPermission]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     country = self.request.query_params.get('country', None)
    #     if country is not None:
    #         queryset = queryset.filter(country__icontains=country)
    #     return queryset


class SupplierFilterView(APIView):
    search_fields = ['country']  # Фильтрация по полю 'country'

    def post(self, request, format=None):
        # Извлечь данные фильтрации из тела POST-запроса
        country = request.data.get('country', None)

        # Провести фильтрацию объектов Suppliers по стране
        if country is not None:
            queryset = Suppliers.objects.filter(country__icontains=country)
            serializer = SupplierSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Missing 'country' parameter"}, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

