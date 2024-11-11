import uuid
from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        FRUITS = "FRUITS"
        VEGETABLES = "VEGETABLES"
        CLOTHES = "CLOTHES"
        TECHNIC = "TECHNIC"

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=Category.choices)
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    price = models.PositiveIntegerField(default=999)

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name}s in {self.stock.name}"
