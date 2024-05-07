from django.contrib import admin
from django.urls import path,include
from contact import views

app_name = 'contact'

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search, name='search'),
    path('add/',views.add, name='add'),
    path('single-contact/<int:num>', views.single_contact, name='single-contact'),
    path('single-contact/delete/<int:num>', views.delete, name='delete'),
    path('single-contact/edit/<int:num>', views.edit, name='edit'),
]