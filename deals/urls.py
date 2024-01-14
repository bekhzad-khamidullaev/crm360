from django.urls import path
from . import views

urlpatterns = [
    path('', views.deals, name='deals'),
    path('delete/<int:deal_id>/', views.delete_deal, name='delete_deal'),
    path('update/<int:deal_id>/', views.update_deal, name='update_deal'),
    path('deals/delete_selected/', views.delete_selected_deals, name='delete_selected_deals'),
]