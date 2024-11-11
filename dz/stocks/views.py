from rest_framework.views import APIView
from rest_framework.response import Response

from stocks.services.product_stock import fetch_product_stock
from stocks.services.stock import fetch_stocks, fetch_stocks_by_id
from stocks.services.product import fetch_product_by_code, fetch_products
from stocks.serializers import (
    ProductSerializer,
    ProductStockSerializer,
    StockSerializer,
)
from rest_framework.request import Request


class ProductListView(APIView):
    def get(self, request: Request) -> Response:
        category = request.query_params.get("category")
        products = fetch_products(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request: Request, code: str) -> Response:
        product = fetch_product_by_code(code=code)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class StockListView(APIView):
    def get(self, request: Request):
        stocks = fetch_stocks()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


class StockProductsListView(APIView):
    def get(self, request: Request, stock_id: int) -> Response:
        stock = fetch_stocks_by_id(stock_id=stock_id)
        products = fetch_product_stock(stock=stock)
        serializer = ProductStockSerializer(products, many=True)
        return Response(serializer.data)
