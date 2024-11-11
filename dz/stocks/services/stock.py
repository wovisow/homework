from stocks.models import Product, Stock
from rest_framework.exceptions import NotFound
from django.db.models.query import QuerySet


def fetch_stocks() -> QuerySet[Stock]:
    return Stock.objects.all()


def fetch_stocks_by_id(*, stock_id: int) -> Stock:
    try:
        return Stock.objects.get(pk=stock_id)
    except Stock.DoesNotExist:
        raise NotFound
