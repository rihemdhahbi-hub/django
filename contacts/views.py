from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Contact

class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Recherche
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(nom__icontains=search_query) |
                Q(prenom__icontains=search_query) |
                Q(email__icontains=search_query) | # Zidna el pipe | hne
                Q(telephone__icontains=search_query)
            )
        # Tri
        sort_by = self.request.GET.get('sort', 'nom')
        if sort_by == 'date_creation':
            queryset = queryset.order_by('-date_creation')
        elif sort_by == 'prenom':
            queryset = queryset.order_by('prenom', 'nom')
        else: # par défaut tri par nom
            queryset = queryset.order_by('nom', 'prenom')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['current_sort'] = self.request.GET.get('sort', 'nom')
        return context

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = ['nom', 'prenom', 'email', 'telephone', 'adresse']
    success_url = reverse_lazy('contacts:list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = ['nom', 'prenom', 'email', 'telephone', 'adresse']
    success_url = reverse_lazy('contacts:list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contacts/contact_confirm_delete.html'
    success_url = reverse_lazy('contacts:list')
