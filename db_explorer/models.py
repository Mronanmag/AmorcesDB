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