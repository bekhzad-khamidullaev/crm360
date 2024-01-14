from django.shortcuts import render, redirect, get_object_or_404
from .models import Deal
from .forms import DealForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
    
def deals(request):
    deals = Deal.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        deals = deals.filter(
            Q(description__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(assigned_to__icontains=search_query) |
            Q(status__icontains=search_query)
        )

    paginator = Paginator(deals, 13)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)
    return render(request, 'deals.html', {'deals': page_items})

def delete_deal(request, deal_id):
    deal = get_object_or_404(Deal, id=deal_id)
    deal.delete()
    return redirect('/deals/')

def delete_selected_deals(request):
    if request.method == 'POST':
        selected_deal_ids = request.POST.getlist('selected_deals')

        if not selected_deal_ids:
            return redirect('/deals/')
        try:
            Deal.objects.filter(id__in=selected_deal_ids).delete()
        except Exception as e:
            return redirect('/deals/')  

        return redirect('/deals/')  

def update_deal(request, deal_id):
    deal = get_object_or_404(Deal, id=deal_id)
    
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('/deals/')
    else:
        form = DealForm(instance=deal)
    
    return render(request, 'deals.html', {'form': form})
