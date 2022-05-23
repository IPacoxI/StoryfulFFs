
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HommeForm
from . import models

# Create your views here.


def dateAjoute(request, id):         # pour afficher les nouveaux ajouts utilisateurs dans la base de données
    date = models.Homme.objects.get( pk = id)
    return render(request, "homme/dateAjoute.html", {"date": date})   # où traitement ==> "affiche(.html)" ==> (dateAjoute)

def update(request, id):
    datei = models.Homme.objects.get(pk=id)
    form = HommeForm(datei.dico())
    return render(request,"homme/ajout.html",{"form":form, "id": id})

def updatetraitement(request, id):
    hommeform = HommeForm(request.POST)
    if hommeform.is_valid():
        homme = hommeform.save(commit = False)
        homme.id = id
        homme.save()
        return HttpResponseRedirect("/antiquite/")
    else:
        return render(request, "homme/ajout.html", {"form": hommeform, "id": id})

def delete(request, id):
    datei = models.Homme.objects.get(pk=id)
    datei.delete()
    return HttpResponseRedirect("/antiquite/")



def ajout(request):
    if request.method == "POST":
        form = HommeForm(request)
        return render(request, "homme/ajout.html", {"form" : form})
    else:
        form = HommeForm()
        id = ""
        return render(request, "homme/ajout.html", {"form": form, "id": id})

def traitement(request):
    hommeform = HommeForm(request.POST)
    if hommeform.is_valid():
        homme = hommeform.save()
        return HttpResponseRedirect("/antiquite/")
    else:
        return render(request, "homme/ajout.html", {"form": hommeform})





