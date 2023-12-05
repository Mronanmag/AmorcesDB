from itertools import product

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django_tables2 import tables, SingleTableView, RequestConfig

from .models import Amorce, Couple
from .forms import AmorceForm, CoupleForm
from .tables import AmorceTable


class BaseView(View):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = {
            'sidebar_items': SidebarView.get_sidebar_items()['items'],
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())


class AccueilView(BaseView):  # Inherit from BaseView
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = AmorceTable(Amorce.objects.all())
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context.update({
            'amorces': Amorce.objects.all(),
            'couples': Couple.objects.all(),
            'table' : table,
        })
        return context


    def get(self, request):
        return render(request, self.template_name, self.get_context_data())


class AmorcesView(BaseView):  # Inherit from BaseView
    template_name = 'forms_html/form_add_primer.html'
    form_primer = AmorceForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'amorces': Amorce.objects.all(),
            'form_primer': self.form_primer,
        })
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        form = AmorceForm(request.POST)
        if form.is_valid():
            amorce_to_save = Amorce()
            amorce_to_save.nom = form.cleaned_data['nom']
            amorce_to_save.orientation = form.cleaned_data['orientation']
            amorce_to_save.sequence = form.cleaned_data['sequence']
            amorce_to_save.temperature_melting = self.metling_temperatre(amorce_to_save.sequence)
            amorce_to_save.taille = self.length_primer(amorce_to_save.sequence)
            amorce_to_save.pourcentage_gc = self.gc_content(amorce_to_save.sequence)
            amorce_to_save.save()
            success_message = f"L'amorce {amorce_to_save.nom} a bien été sauvegardée dans la base de données."
            context = self.get_context_data()
            context['success_message'] = success_message
            return render(request, self.template_name, context)
        else:
            raisons = form.errors
            success_message = f"L'amorce n'a pas été sauvegardée dans la base de données pour les raisons suivantes : {raisons}"
            context = self.get_context_data()
            context['form_primer'] = form
            return render(request, self.template_name, context)

    def length_primer(self, sequence):
        return len(sequence)

    def gc_content(self, sequence):
        gc_content_value = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        return round(gc_content_value, 2)

    def metling_temperatre(self, seq):
        if seq.count('A') + seq.count('T') + seq.count('G') + seq.count('C') != len(seq):
            liste_amorces = self.remplacer_bases_degeneres(seq)
            print(liste_amorces)
        return 15

    def remplacer_bases_degeneres(self, primer):
        bases_degeneres = {
            'R': ['A', 'G'],
            'Y': ['C', 'T'],
            'S': ['G', 'C'],
            'W': ['A', 'T'],
            'K': ['G', 'T'],
            'M': ['A', 'C'],
            'B': ['C', 'G', 'T'],
            'D': ['A', 'G', 'T'],
            'H': ['A', 'C', 'T'],
            'V': ['A', 'C', 'G'],
            'N': ['A', 'C', 'G', 'T']
        }
        liste_primer = [''.join(p) for p in product(*[bases_degeneres.get(base, [base]) for base in primer])]
        return list(set(liste_primer))


class CouplesView(BaseView):
    template_name = 'forms_html/form_add_couple.html'
    form_couple = CoupleForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'amorces': Amorce.objects.all(),
            'form_couple': self.form_couple,
        })
        return context

    def post(self, request):
        form = CoupleForm(request.POST)
        if form.is_valid():
            couple_instance = form.save()
            amorce_forward_nom = form.cleaned_data['amorce_forward'].nom
            amorce_reverse_nom = form.cleaned_data['amorce_reverse'].nom
            success_message = f"Le couple {couple_instance.nom} avec les amorces {amorce_forward_nom} et {amorce_reverse_nom} a bien été sauvegardé dans la base de données."
            context = self.get_context_data()
            context['success_message'] = success_message
            return render(request, self.template_name, context)
        else:
            raisons = form.errors
            success_message = f"Le couple n'a pas été sauvegardé dans la base de données pour les raisons suivantes : {raisons}"
            context = self.get_context_data()
            context['form_couple'] = form
            return render(request, self.template_name, context)


def get(self, request):
    context = self.get_context_data()
    return render(request, self.template_name, context)


class SidebarView():
    @staticmethod
    def get_sidebar_items():
        items = [
            {'href': 'index', 'label': 'Accueil', 'icon': 'fas fa-home'},
            {'href': 'amorces', 'label': 'Amorces', 'icon': 'fas fa-fish'},
            {'href': 'couples', 'label': 'Couples', 'icon': 'fas fa-users'},
            {'href': 'admin:index', 'label': 'Admin', 'icon': 'fas fa-cogs'}
        ]
        return {'items': items}

