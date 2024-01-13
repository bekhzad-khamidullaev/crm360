from django.urls import path
from . import views

urlpatterns = [
    path('', views.leads, name='leads'),
    path('leads/<int:pk>/', views.lead_detail, name='lead_detail'),
    path('get_leads/', views.get_leads, name='get_leads'),
    path('update_lead_status/<int:lead_id>/', views.update_lead_status, name='update_lead_status'),

]
