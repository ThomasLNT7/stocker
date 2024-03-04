from django.db import models


# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    prix = models.FloatField(default=0)
    image = models.ImageField(upload_to="")
    quantite = models.IntegerField()


class Magasin(models.Model):
    nom = models.CharField(max_length=200, default="Magasin")
    adp = models.CharField(max_length=400)
    cp = models.CharField(max_length=20)
    ville = models.CharField(max_length=100)
    adm = models.CharField(max_length=400)
    adt = models.CharField(max_length=50)
    produits = models.ManyToManyField(Produit)
