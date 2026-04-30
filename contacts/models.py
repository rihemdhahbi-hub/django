from django.db import models
from django.urls import reverse

class Contact(models.Model):
    nom = models.CharField('Nom', max_length=100)
    prenom = models.CharField('Prénom', max_length=100)
    email = models.EmailField('Adresse email', blank=True, null=True)
    telephone = models.CharField('Téléphone', max_length=20, blank=True)
    adresse = models.TextField('Adresse', blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nom', 'prenom']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    def get_absolute_url(self):
        return reverse('contacts:detail', kwargs={'pk': self.pk})