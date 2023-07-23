from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizations, name='organizations')

]
