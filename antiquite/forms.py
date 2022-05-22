from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AntiquiteForm(ModelForm):
    class Meta :
        model = models.Antiquite
        fields = ('periode', 'peuple', 'evenement_associe', 'resume') #homme_appartenance
        labels = {
            'periode' : _('Période'),
            'peuple' : _('Peuple'),
            'evenement_associe' : _('Evénement_associé'),
            'resume' : _('Résumé'),
        }

class HommeForm(ModelForm):
    class Meta :
        model = models.Homme
        fields = ('epoque_appartenance',)
        labels = {
            'epoque_appartenance' : _('Appartenance de l époque'),
        }
