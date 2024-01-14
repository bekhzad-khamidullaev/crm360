from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizations, name='organizations'),
    path('company/<int:pk>/', views.company_detailed, name='company_detailed'),

]
