from django.urls import path
from . import views

urlpatterns = [
    path('', views.leads, name='leads'),
    path('leads/<int:pk>/', views.lead_detail, name='lead_detail'),
]
