from django.shortcuts import render
from django.views.generic import View
from .models import Product
from django.shortcuts import render, get_object_or_404

# Create your views here.

class ProductList(View):
    def get(self, request):
        products = Product.objects.filter(available = True)
        return render(request, "shop/products_list.html", {"products":products,})


def product_detail(request, id, slug):
    post = get_object_or_404(Product, id = id, slug = slug)
    return render(request, "shop/product_detail.html", {"product":post})
