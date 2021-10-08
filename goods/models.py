from django.db import models

# TODO use real model

class Flower(models.Model):




class Product:
    @staticmethod
    def all():
        return [
            {
                "id": 1,
                "title": "Test Product",
                "count": 100,
            },
            {
                "id": 2,
                "title": "Flower",
                "count": 2,
            },
            {
                "id": 3,
                "title": "Car",
                "count": 0,
            },
        ]
