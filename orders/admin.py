from django.contrib import admin
from orders.models import Cart, CartItem

admin.site.register(Cart)
admin.site.register(CartItem)
