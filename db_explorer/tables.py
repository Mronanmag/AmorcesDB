import django_tables2 as tables
from .models import Amorce

class AmorceTable(tables.Table):
    nom = tables.Column(verbose_name='Nom de l\'amorce')
    description = tables.Column(verbose_name='Description')

    class Meta:
        model = Amorce
        attrs = {'class': 'table table-striped table-bordered'}  # Exemple de classe CSS pour la mise en forme
        sequence = ('nom', 'description')  # Ordre des colonnes