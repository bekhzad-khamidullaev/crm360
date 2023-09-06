from django.shortcuts import render
from .models import Lead

def leads(request):
    leads = Lead.objects.all()
    return render(request, 'leads_table.html', {'leads': leads})


def lead_detail(request, pk):
    leads = Lead.objects.all()
    return render(request, 'leads_detail.html', {'leads': leads})