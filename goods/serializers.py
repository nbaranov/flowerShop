from rest_framework import serializers
from goods.models import Product, Favorite


class ProductListCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', "title", "description", "quantity", "price"]


class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'products']
