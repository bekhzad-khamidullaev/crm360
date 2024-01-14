from django.shortcuts import render, get_object_or_404
from .models import Products
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q

def products(request):
    products = Products.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(id__in=search_query) |
            # Q(status__contains=search_query) |
            # Q(lead__contains=search_query) |
            Q(price__in=search_query) |
            Q(name__contains=search_query) |
            Q(description__contains=search_query)
            
        )

    paginator = Paginator(products, 15)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)
    return render(request, 'products.html', {'products': page_items})

def product_detail(request, pk):
    product_detail = get_object_or_404(Products, pk=pk)
    return render(request, 'product_detailed.html', {'product': product_detail})