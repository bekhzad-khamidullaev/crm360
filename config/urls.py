from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),
    path('', include('users.urls')),
    path('contacts/', include('contacts.urls')),
    path('deals/', include('deals.urls')),
    path('products/', include('products.urls')),
    path('organizations/', include('organizations.urls')),
]
