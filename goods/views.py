from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser


from goods.models import Product
from goods.serializers import ProductListCustomerSerializer
from goods.services import ProductService
from goods.utils import ExcelParser


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


class ProductImportFromExcelFile(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        # todo проверить работоспособность
        file = request.FILES['file']
        parser = ExcelParser()
        ProductService.load_many_from_file(file, parser)

        return Response(status=204)
