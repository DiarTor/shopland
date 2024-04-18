from django.http import Http404
from django.shortcuts import render,get_object_or_404

from product_module.models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_module/product_list.html', {"products": products})


def product_detail(request, product_id):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404("Product does not exist")
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_module/product_detail.html', {"product": product})
