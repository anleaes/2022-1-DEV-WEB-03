import imp
from socket import fromshare
from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        exclude = ('created_on', 'updated_on')