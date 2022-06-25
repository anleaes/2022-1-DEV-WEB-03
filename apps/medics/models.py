from django.db import models

# Create your models here.

class Medic(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=200)
    crm = models.CharField('CRM', max_length=10)
    spec = models.CharField('Especialidade', max_length=100)
    address = models.CharField('Endereco', max_length=100)
    phone = models.CharField('Telefone', max_length=20)
    
    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        ordering =['id']

    def __str__(self):
        return self.name
