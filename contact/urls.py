from django.contrib import admin
from django.urls import path
from contact import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'contact'

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search, name='search'),
    path('add/',views.add, name='add'),
    path('single-contact/<int:num>', views.single_contact, name='single-contact'),
    path('single-contact/delete/<int:num>', views.delete, name='delete'),
    path('single-contact/edit/<int:num>', views.edit, name='edit'),
    path('user/register',views.register,name='register'),
    path('user/login', views.login_view,name='login'),
    path('user/logout', views.logout_view,name='logout'),
    path('user/login/change_password', views.change_password, name='chpassword'),
    path('user/login/delete', views.delete_user, name='delete-user'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)