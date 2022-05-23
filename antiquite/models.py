from django.db import models

# Create your models here.

class Antiquite(models.Model):
    periode = models.IntegerField(blank = False, null = False)
    peuple = models.CharField(max_length=100)
    evenement_associe = models.CharField(max_length=100)
    resume = models.TextField(null = True, blank = True)


    def __str__(self):
        chaine = f"{self.evenement_associe} eut lieu aux alentours {self.periode} et concerne les {self.peuple}"
        return chaine

    def dico(self):
        return {"evenement_associe":self.evenement_associe, "periode":self.periode, "peuple":self.peuple, "resume":self.resume}

class Homme(models.Model):
    epoque_appartenance = models.ForeignKey(Antiquite, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "homme"

    def dico(self):
        return {"epoque_appartenance" : self.epoque_appartenance}
 
