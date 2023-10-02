from django.urls import path
from . import views
from django.views.generic import ListView


app_name = "products"

urlpatterns = [
    path("", views.Category.as_view(), name="category"),
    path("product/", views.Product.as_view(), name="products"),
    path("subcategorie/", views.SubCategory.as_view(), name="subcategory"),

]
