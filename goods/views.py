from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Product
from goods.serializers import ProductListCustomerSerializer 

class PaginatorAPI(PageNumberPagination):
    page_size = 2


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        paginated_page = PaginatorAPI().paginate_queryset(products, request)
        serializer = ProductListCustomerSerializer(paginated_page, many=True)
        
        return Response(serializer.data)

