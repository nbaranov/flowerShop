from django.shortcuts import redirect
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import GenericViewSet

from goods.models import Product, Favorite
from goods.serializers import ProductListCustomerSerializer, FavoriteListSerializer
from goods.services import ProductService
from goods.utils import ExcelParser, CsvParser
from users.permissions import IsProfileOwnerOrAdmin


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

    def post(self, request):
        parsers = {
            'xlsx': ExcelParser(),
            'csv': CsvParser(),
        }
        file = request.FILES['file']
        try:
            file_type = str(request.FILES['file']).split('.')[-1]
            parser = parsers[file_type]
        except KeyError:
            raise ImportError('Неверный формат файла. Используйте .csv или .xlsx')
        ProductService.load_many_from_file(file, parser)

        return redirect('products_list')


class FavoriteViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = Favorite.objects.all()
    permission_classes = (IsProfileOwnerOrAdmin,)
    serializer_class = FavoriteListSerializer
