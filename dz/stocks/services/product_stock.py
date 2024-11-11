from stocks.models import ProductStock, Stock
from django.db.models.query import QuerySet


def fetch_product_stock(*, stock: Stock) -> QuerySet[ProductStock]:
    return ProductStock.objects.filter(stock=stock)
