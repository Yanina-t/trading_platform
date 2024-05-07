from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Suppliers, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Все поля модели будут сериализованы


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'  # Все поля модели будут сериализованы

    def update(self, instance, validated_data):
        # Переопределение метода update для запрета обновления поля 'debt_to_supplier'
        if 'debt_to_supplier' in validated_data:
            raise serializers.ValidationError("Обновление поля 'Задолженность (debt_to_supplier)' через API запрещено.")
        return super().update(instance, validated_data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username

        return token
