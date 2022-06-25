from django.db import models

# Create your models here.

class Pacient(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=10)
    bdate = models.CharField('Data de Nascimento', max_length=50)
    address = models.CharField('Endereco', max_length=100)
    phone = models.CharField('Telefone', max_length=20)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering =['id']

    def __str__(self):
        return self.name
