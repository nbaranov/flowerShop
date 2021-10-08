from rest_framework import serializers
from goods.models import Product



class ProductListCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', "title", "description", "quantity", "price"]
