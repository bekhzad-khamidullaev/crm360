from django.shortcuts import render, get_object_or_404
from .models import Contacts
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import ContactsForm
from django.views.generic import DeleteView

def contacts(request):
    contacts = Contacts.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        contacts = contacts.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query)

        )
    paginator = Paginator(contacts, 13)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)
    return render(request, 'contacts.html', {'contacts':page_items})

def contact_detail(request, pk):
    contact = get_object_or_404(Contacts, pk=pk)
    return render(request, 'contact_detailed.html', {'contact': contact})


def delete_contact(request, contact_id):
    contact = get_object_or_404(contact, id=contact_id)
    contact.delete()
    return redirect('/contacts/')

def delete_selected_contacts(request):
    if request.method == 'POST':
        selected_contact_ids = request.POST.getlist('selected_contacts')

        if not selected_contact_ids:
            return redirect('/contacts/')
        try:
            Contacts.objects.filter(id__in=selected_contact_ids).delete()
        except Exception as e:
            return redirect('/contacts/')  

        return redirect('/contacts/')  

def update_contact(request, contact_id):
    contact = get_object_or_404(contact, id=contact_id)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/contacts/')
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'contacts.html', {'form': form})