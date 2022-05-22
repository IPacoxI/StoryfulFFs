from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AntiquiteForm
from . import models

# Create your views here.

def index(request):
    liste = list(models.Antiquite.objects.all())
    return render(request, "antiquite/index.html", {"liste" : liste})

def dateAjoute(request, id):         # nouvel usage de traitement.html pour afficher les nouveaux ajouts utilisateurs dans la base de données
    antiquite = models.Antiquite.objects.get( pk = id)
    homme = models.Homme.objects.filter(epoque_appartenance=antiquite.id)
    return render(request, "antiquite/dateAjoute.html", {"antiquite": antiquite, "homme": homme})    #  en envoyant variable antiquite


def update(request, id):
    datei = models.Antiquite.objects.get(pk=id)
    form = AntiquiteForm(datei.dico())
    return render(request,"antiquite/ajout.html",{"form":form, "id": id})

def updatetraitement(request, id):
    antform = AntiquiteForm(request.POST)
    if antform.is_valid():
        antiquite = antform.save(commit = False)
        antiquite.id = id
        antiquite.save()
        return HttpResponseRedirect("/antiquite/")
    else:
        return render(request, "antiquite/ajout.html", {"form": antform, "id": id})

def delete(request, id):
    datei = models.Antiquite.objects.get(pk=id)
    datei.delete()
    return HttpResponseRedirect("/antiquite/")




def ajout(request):
    if request.method == "POST":
        form = AntiquiteForm(request)
        return render(request, "antiquite/ajout.html", {"form" : form})
    else:
        form = AntiquiteForm()
        id = ""
        return render(request, "antiquite/ajout.html", {"form": form, "id" : id})

def traitement(request):
    antform = AntiquiteForm(request.POST)
    if antform.is_valid():
        antiquite = antform.save()
        return HttpResponseRedirect("/antiquite/")
    else:
        return render(request, "antiquite/ajout.html", {"form": antform})



def saisie(request):
    return render(request,"antiquite/saisie.html")



def frise(request):
    return render(request, "antiquite/frise.html")