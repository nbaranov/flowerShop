from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

from goods.models import Product


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_item')
    quantity_in_cart = models.IntegerField(validators=[MinValueValidator(1)], default=1)
