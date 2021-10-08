from django.urls import path

from goods.views import ProductList

urlpatterns = [
    path('', ProductList.as_view(), name='products_list')
]
