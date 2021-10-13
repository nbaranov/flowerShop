from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


from goods.models import Product
from goods.serializers import ProductListCustomerSerializer 

class PaginatorAPI(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListCustomerSerializer
    pagination_class = PaginatorAPI
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
