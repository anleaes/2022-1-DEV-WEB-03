from django import forms
from .models import Pacient

class PacientForm(forms.ModelForm):
    
    class Meta:
        model = Pacient
        exclude = ('created_on', 'updated_on',)
