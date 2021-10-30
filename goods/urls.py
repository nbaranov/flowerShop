from django.urls import path

from goods.views import ProductList, ProductImportFromExcelFile

urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path('import', ProductImportFromExcelFile.as_view(), name='product_import'),
]
