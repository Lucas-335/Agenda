from django.db import models

# Create your models here.

class Contact(models.Model):
    
    name = models.CharField(
        verbose_name='Nome',
        max_length=255,
        null=False,
        )
    last_name = models.CharField(
        verbose_name='Sobrenome',
        max_length=255,
        null=False,
    )
    number = models.IntegerField(
        verbose_name='Telefone',
        max_length=13,
        null=False,
        )
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        blank=True,
        default='',
    )
    category = models.ForeignKey(
        to='Categories',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default='',
        related_name='+')

    def __str__(self):
        return f'{self.name} {self.last_name}'
    
class Categories(models.Model):
    categories = models.CharField(
        verbose_name='Categoria',
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return f'{self.categories}'
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    