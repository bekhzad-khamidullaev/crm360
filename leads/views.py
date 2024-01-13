from django.shortcuts import render, get_object_or_404
from .models import Lead
from django.http import JsonResponse
from django.views.decorators.http import require_POST



def leads(request):
    leads = Lead.objects.all()
    return render(request, 'leads_list.html', {'leads': leads})


def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads_detailed.html', {'lead': lead})


def leads_board(request):
    return render(request, 'leads_board.html')

def get_leads(request):
    status = request.GET.get('status', 'new')
    leads = Lead.objects.filter(status=status).order_by('lead_id')
    data = [{'lead_id': lead.lead_id, 'product_name': lead.product_name, 'customer': lead.customer,
             'email': lead.email, 'source': lead.source, 'contact_date': lead.contact_date} for lead in leads]
    return JsonResponse(data, safe=False)

@require_POST
def update_lead_status(request, lead_id):
    new_status = request.POST.get('status')
    try:
        lead = Lead.objects.get(lead_id=lead_id)
        lead.status = new_status
        lead.save()
        return JsonResponse({'message': 'Lead status updated successfully.'})
    except Lead.DoesNotExist:
        return JsonResponse({'error': 'Lead not found.'}, status=404)