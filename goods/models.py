from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.title}"


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    products = models.ManyToManyField(Product, through="FavoriteProductList")

    def __str__(self):
        queryset = FavoriteProductList.objects.filter(fav_user = self).values('product__title')
        product_list = [product['product__title'] for product in queryset]
        return f"{self.user.username}: {', '.join(product_list)}"


class FavoriteProductList(models.Model):
    fav_user = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fav_user.user.username}: {self.product}"