from django.db import models

class Amorce(models.Model):
    nom = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100, choices=[('forward', 'forward'), ('reverse', 'reverse')])
    sequence = models.CharField(max_length=100)
    taille = models.IntegerField()
    pourcentage_gc = models.FloatField()
    temperature_melting = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom + '_' + self.orientation

class Couple(models.Model):
    nom = models.CharField(max_length=100)
    amorce_forward = models.ForeignKey(Amorce, on_delete=models.CASCADE, related_name='amorce_forward')
    amorce_reverse = models.ForeignKey(Amorce, on_delete=models.CASCADE, related_name='amorce_reverse')
    taille_fragment = models.IntegerField()
    programme_pcr = models.CharField(max_length=10000)
    region = models.CharField(max_length=100)
    bibliographie = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Echantillon(models.Model) :
    code_interne = models.CharField(max_length=100)
    code_client = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_reception = models.DateField()
    date_rendu = models.DateField()
    date_suppression = models.DateField()
    type_barcode = models.CharField(max_length=100)

    def __str__(self):
        return self.code_interne + '_' + self.code_client


class Librairie(models.Model) :
    nom_librairie = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    finished = models.BooleanField()


class Couple_Echantillon(models.Model):
    id_couple = models.ForeignKey(Couple, on_delete=models.CASCADE)
    id_echantillon = models.ForeignKey(Echantillon, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_couple + '_' + self.id_echantillon


class Librairie_Echantillon(models.Model):
    id_librairie = models.ForeignKey(Librairie, on_delete=models.CASCADE)
    id_echantillon = models.ForeignKey(Echantillon, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_librairie + '_' + self.id_echantillon