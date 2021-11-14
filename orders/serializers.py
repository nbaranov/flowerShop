from rest_framework import serializers

from goods.serializers import ProductListCustomerSerializer
from orders.models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListCustomerSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('product', 'quantity_in_cart')


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user_id', 'items')
