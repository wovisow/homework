from stocks.models import Product
from rest_framework.exceptions import NotFound, ValidationError
from django.db.models.query import QuerySet


def fetch_products(*, category: str = None) -> QuerySet[Product]:
    if category is not None:
        category = category.upper()
        if category not in Product.Category:
            raise ValidationError

        return Product.objects.filter(category=category.upper())

    return Product.objects.all()


def fetch_product_by_code(*, code: str) -> Product:
    try:
        return Product.objects.get(code=code)
    except Product.DoesNotExist:
        raise NotFound
