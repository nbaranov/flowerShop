from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from goods.views import ProductList, ProductImportFromFile, FavoriteViewSet

router = DefaultRouter()
router.register(r'favorite', FavoriteViewSet, basename='products_favorites')

urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path('import', ProductImportFromFile.as_view(), name='products_import'),
    *router.urls,

]
