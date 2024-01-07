from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),
    path('', include('users.urls')),
    path('contacts/', include('contacts.urls')),
    path('deals/', include('deals.urls')),
    path('products/', include('products.urls')),
    path('organizations/', include('organizations.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
