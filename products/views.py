from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from . models import *

# Create your views here.


class Index(TemplateView):
    template_name = "products/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class CategoryListView(ListView):
    model = Category
    template_name = "products/category.html"

class SubCategory(ListView):
    model = SubCategory
    template_name = "products/subcategory.html"  

class Product(ListView):
    model= Product
    template_name = "products/product.html"
