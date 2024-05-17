from django.contrib import admin
from .models import Contact, Categories
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Contato',
            {
                'fields':[('name','last_name'),'number','email','category','image'],
                'description':['Informações do contato']
            }
        ),
    ]
    list_display = ['id','name','last_name']
    list_per_page = 5
    list_max_show_all = 50
    ordering = ['-id']

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Categoria',
            {
                'fields':['categories'],
                'description':['Categorias de contato']
            }
        )
    ]
    list_display = ['categories']
    
    