from django.contrib import admin

from .models import Product, Stock, ProductStock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = [
        "category",
        "code",
        "price",
    ]
    list_display = [
        "pk",
        "description",
        "category",
        "code",
        "price",
    ]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
        "address",
    ]
    list_display = [
        "pk",
        "name",
        "address",
    ]


@admin.register(ProductStock)
class ProductStockAdmin(admin.ModelAdmin):
    search_fields = [
        "product__name",
        "stock__name",
        "quantity",
    ]
    list_display = [
        "pk",
        "stock",
        "product",
        "quantity",
    ]
