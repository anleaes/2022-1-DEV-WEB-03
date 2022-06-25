from django import forms
from .models import Medic

class MedicForm(forms.ModelForm):
    
    class Meta:
        model = Medic
        exclude = ('created_on', 'updated_on',)