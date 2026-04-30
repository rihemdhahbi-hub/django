from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'telephone', 'date_creation')
    list_filter = ('date_creation',)
    search_fields = ('nom', 'prenom', 'email', 'telephone')
    ordering = ('nom', 'prenom')