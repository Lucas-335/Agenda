from django.contrib import admin
from django.urls import path,include
from form import views

namespace = 'form'

urlpatterns = [
    path('',views.index,name='index')
]