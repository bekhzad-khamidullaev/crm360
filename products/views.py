from django.shortcuts import render, get_object_or_404
from .models import Products

def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, pk):
    product_detail = get_object_or_404(Products, pk=pk)
    return render(request, 'product_detailed.html', {'product': product_detail})