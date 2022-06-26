from django.db import models
from schedules.models import Schedule
from pacients.models import Pacient

# Create your models here.

class Exam(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField('Data de Realizacao')
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'
        ordering =['id']

    def __str__(self):
        return self.schedule