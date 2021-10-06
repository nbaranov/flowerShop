from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Product
from goods.serializers import ProductListCustomerSerializer


class ProductList(APIView):
    # TODO use generic class-based view
    def get(self, request):
        products = Product.all()
        serializer = ProductListCustomerSerializer(products, many=True)
        return Response(serializer.data)
