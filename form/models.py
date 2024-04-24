from django.db import models

# Create your models here.

class Contact(models.Model):
    
    name = models.CharField(
        verbose_name='Nome',
        max_length=255,
        )
    last_name = models.CharField(
        verbose_name='Sobrenome',
        max_length=255,
    )
    number = models.IntegerField(
        verbose_name='Telefone',
    )