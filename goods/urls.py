from django.urls import path

from goods.views import ProductList, ProductImportFromFile

urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path('import', ProductImportFromFile.as_view(), name='product_import')
]
