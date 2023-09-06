from django.shortcuts import render

def products(request):
    return render(request, 'products.html')

def kanban(request):
    return render(request, 'kanban.html')