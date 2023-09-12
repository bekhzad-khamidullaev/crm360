from django.shortcuts import render
from .models import Products

def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products': products})


def product_detail(request):
    product_detail = Products.objects.all()
    return render(request, 'products_detail.html', {'product': product_detail})
