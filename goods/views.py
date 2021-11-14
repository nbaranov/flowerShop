from django.shortcuts import redirect
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
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
    GenericViewSet,
):
    queryset = Favorite.objects.all()
    permission_classes = (IsProfileOwnerOrAdmin,)
    serializer_class = FavoriteListSerializer

    # todo подумать как удалить возможность замены избранного (put),
    #  как следствие - отдельный эндпоинт для удаления из избранного
    # todo методы для создания и удаления "избранного"

    def partial_update(self, request, pk=None):
        db_favorite_data = self.queryset.get(user_id=request.user.pk)
        for product_id in request.data['products']:
            product = Product.objects.filter(id=product_id)
            if product.exists():
                product = product[0]
                db_favorite_data.products.add(product)
                db_favorite_data.save()
            else:
                raise ValueError(f'В БД нет продукта с id {product_id}')

            db_products = db_favorite_data.products.all().values('id')
            serialized_data = {
                "user": db_favorite_data.serializable_value('user'),
                "products": [item.get('id') for item in db_products]
            }
            serializer = FavoriteListSerializer(request.user, data=serialized_data, partial=True)

        return Response(serializer.initial_data)
