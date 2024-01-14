from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('update/<int:pk>/', views.update_contact, name='update_contact'),
]
