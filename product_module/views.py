from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from product_module.models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all().order_by('title')
    total_products = products.count()
    return render(request, 'product_module/product_list.html',
                  {"products": products, "total_products": total_products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', {"product": product})
