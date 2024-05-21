from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User
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
    image = models.ImageField(
        verbose_name='Foto',
        blank=True,
        null=True,
        upload_to='media/photos',
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.name} {self.last_name}'
    
    def resize_img(self,img):
        import os
        _name, _type = os.path.splitext(img.__str__())
        size=(150,200)
        
        with Image.open(img) as im:
            im = im.resize(size)
            im_io = BytesIO() 
            im.save(im_io, 'JPEG', quality=100, optimize=True) 

            new_image = File(im_io, name=img.name)
            return new_image

    def save(self, *args, **kwargs):
        if self.image:
            new_image = self.resize_img(self.image)
            self.image = new_image
        return super().save(*args, **kwargs)

        # size = (100,150)
        # with Image.open(img) as im:
        #     ImageOps.contain(im,size).save(f'{img.__str__()}.jpg')

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
        
    