from django.db import models

from medics.models import Medic
from pacients.models import Pacient

# Create your models here.

class Schedule(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type = models.CharField('Tipo de Exame', max_length=50)
    date = models.DateField('Data do Exame', auto_now=False, auto_now_add=False) 
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE)
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering =['id']

    def __str__(self):
        return self.type