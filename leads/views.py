from django.shortcuts import render
<<<<<<< HEAD
from .models import Lead

def leads(request):
    leads = Lead.objects.all()
    return render(request, 'leads_table.html', {'leads': leads})


def lead_detail(request, pk):
    leads = Lead.objects.all()
    return render(request, 'leads_detail.html', {'leads': leads})
=======
from .models import Leads

def leads(request):
    return render(request, 'leads.html')


def lead_detail(request):
    leads = Leads.objects.all()
    return render(request, 'lead_detail.html', {'leads': leads})
>>>>>>> e039bc4e4e6d77f5b95067663c9e0c973901d6bc
