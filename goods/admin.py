from django.contrib import admin
from goods.models import Favorite, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Favorite)
