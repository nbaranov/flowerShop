from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser


from goods.models import Product
from goods.serializers import ProductListCustomerSerializer 
from goods.utils import read_excel


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


class ProductImportFromFile(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file = request.FILES['file']
        print(file)
        data_table = read_excel(file, number_of_cols=4)
        for row in data_table:
            product = Product.objects.create(title = row[0],
                                             description = row[1],
                                             quantity = row[2],
                                             price = row[3])
            product.save()

        

        return Response(status=204)