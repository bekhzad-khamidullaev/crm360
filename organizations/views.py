from .models import Company
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

def organizations(request):
    companies = Company.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        companies = companies.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(industry__icontains=search_query) |
            Q(website__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(address__icontains=search_query)
        )

    paginator = Paginator(companies, 13)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)
    return render(request, 'companies.html', {'companies': page_items})


def company_detailed(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company_detailed.html', {'company': company})
