from django.urls import path
from . import views
app_name = 'contacts'
urlpatterns = [
path('', views.ContactListView.as_view(), name='list'),
path('ajouter/', views.ContactCreateView.as_view(), name='add'),
path('<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
path('modifier/<int:pk>/', views.ContactUpdateView.as_view(), name='edit'),
path('supprimer/<int:pk>/', views.ContactDeleteView.as_view(), name='delete'),
]