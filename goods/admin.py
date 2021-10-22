from django.contrib import admin
from goods.models import Favorite, Product, FavoriteProductList

# Register your models here.
admin.site.register(Product)
admin.site.register(Favorite)
admin.site.register(FavoriteProductList)
