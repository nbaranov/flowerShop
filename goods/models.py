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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user}: {self.products.all()}"
