from django.urls import path
from . import views
from .views import ProductListView,ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
    # path("product-favorite/",AddProductFavorite.as_view(),name="Product_favorite")
]