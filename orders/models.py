from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

from goods.models import Product


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductInCart')

    def __str__(self):
        return f"{self.user}"


class ProductInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

