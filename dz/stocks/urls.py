from django.urls import include, path

from .views import (
    ProductDetailView,
    ProductListView,
    StockListView,
    StockProductsListView,
)

urlpatterns = [
    path(
        "products/",
        include(
            [
                path("", ProductListView.as_view(), name="product-list"),
                path(
                    "<str:code>/",
                    ProductDetailView.as_view(),
                    name="product-detail",
                ),
            ]
        ),
    ),
    path(
        "stocks/",
        include(
            [
                path("", StockListView.as_view(), name="stock-list"),
                path(
                    "<int:stock_id>/products/",
                    StockProductsListView.as_view(),
                    name="stock-products",
                ),
            ]
        ),
    ),
]
