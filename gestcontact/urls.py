from django.contrib import admin
from django.urls import path, include # Mathabbat elli famma kelmet "include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')), # Hedhi l'ligne elli t'rabat'hom b'ba3dh'hom
]