from rest_framework import serializers

from stocks.models import Product, ProductStock, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class ProductStockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    stock = StockSerializer()

    class Meta:
        model = ProductStock
        fields = ["product", "stock", "quantity"]
