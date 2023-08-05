from django.shortcuts import render
from .models import Leads

def leads(request):
    return render(request, 'leads.html')


def lead_detail(request):
    leads = Leads.objects.all()
    return render(request, 'lead_detail.html', {'leads': leads})