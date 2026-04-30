from django.urls import path
from . import views

# Hedhi app_name mta3 el dossier contacts
app_name = 'contacts'

urlpatterns = [
    # Saf7at el lista (index)
    path('', views.ContactListView.as_view(), name='list'),
    
    # Saf7at el details mta3 contact (bi pk ya3ni id)
    path('<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    
    # Saf7at el creation (sna3 contact jdid)
    path('nouveau/', views.ContactCreateView.as_view(), name='create'),
    
    # Saf7at el modification
    path('<int:pk>/modifier/', views.ContactUpdateView.as_view(), name='update'),
    
    # Saf7at el supprimer
    path('<int:pk>/supprimer/', views.ContactDeleteView.as_view(), name='delete'),
]