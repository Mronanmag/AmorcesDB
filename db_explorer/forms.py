from django import forms
from .models import Amorce, Couple

class AmorceForm(forms.ModelForm):
    class Meta:
        model = Amorce
        fields = 'nom', 'orientation', 'sequence', 'temperature_melting'

    def clean(self):
        #Vérifie que les séquences ne sont pas vides
        cleaned_data = super().clean()
        sequence = cleaned_data.get("sequence")
        if sequence == "":
            raise forms.ValidationError("La séquence ne peut pas être vide")
        #Vérifie que la séquence ne contient que des nucléotides
        autorised_nucleotides = ['A', 'T', 'C', 'G', 'N','R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V']
        sequence = cleaned_data.get("sequence").upper()
        print(sequence)
        for nucleotide in sequence :
            print(nucleotide)
            if nucleotide not in autorised_nucleotides:
                raise forms.ValidationError("La séquence contient des caractères non autorisés")
        return cleaned_data

class CoupleForm(forms.ModelForm):
    class Meta:
        model = Couple
        fields = '__all__'

    def clean(self):
        #Vérifie que le couple d'amorces n'existe pas déja (dans les deux sens)
        cleaned_data = super().clean()
        amorce_forward = cleaned_data.get("amorce_forward")
        amorce_reverse = cleaned_data.get("amorce_reverse")
        if amorce_forward == amorce_reverse:
            raise forms.ValidationError("Les amorces doivent être différentes")
        if Couple.objects.filter(amorce_forward=amorce_forward, amorce_reverse=amorce_reverse).exists():
            raise forms.ValidationError("Ce couple d'amorces existe déjà")
        if Couple.objects.filter(amorce_forward=amorce_reverse, amorce_reverse=amorce_forward).exists():
            raise forms.ValidationError("Ce couple d'amorces existe déjà")
        #Vérifie si le nom du couple n'existe pas déja
        nom = cleaned_data.get("nom")
        if Couple.objects.filter(nom=nom).exists():
            raise forms.ValidationError("Ce nom de couple existe déjà")

        return cleaned_data