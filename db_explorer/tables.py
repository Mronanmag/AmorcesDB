import django_tables2 as tables
from .models import Amorce, Couple


class AmorceTable(tables.Table):
    nom = tables.Column(verbose_name='Nom de l\'amorce')

    class Meta:
        model = Amorce
        attrs = {'class': 'table table-striped table-bordered'}  # Exemple de classe CSS pour la mise en forme

class CoupleTable(tables.Table):
    nom = tables.Column(verbose_name='Nom du couple')

    class Meta:
        model = Couple
        attrs = {'class': 'table table-striped table-bordered'}  # Exemple de classe CSS pour la mise en forme
