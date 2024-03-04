from django.shortcuts import render
from .models import Produit
from .models import Magasin

# Create your views here.

def index(request):
    produit = Produit.objects.all()
    magasin = Magasin.objects.all()
    return render(request, 'menu/index.html', {"Produit": produit, "Magasin": magasin})