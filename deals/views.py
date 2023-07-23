from django.shortcuts import render

def deals(request):
    return render(request, 'deals.html')

