# alpe/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),       # Django admin site
    path('', include('webapp.urls')),      # Include webapp URLs directly
]