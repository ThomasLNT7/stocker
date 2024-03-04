from django.contrib import admin
from .models import Produit
from .models import Magasin


class ProduitAdmin(admin.ModelAdmin):
    list_display = ("image", "nom", "prix", "quantite")
    search_fields = ["nom"]

class MagasinAdmin(admin.ModelAdmin):
    list_display = ("nom", "adp", "adm")
    search_fields = ["nom"]


# Register your models here.
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Magasin, MagasinAdmin)
