from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monapp.urls')),  # Inclure les URLs de votre application
]
