from django import forms
from .import models

class InscricaoForm(forms.ModelForm):
       

      class Meta:
            model = models.Inscricao
            fields = "__all__" 

