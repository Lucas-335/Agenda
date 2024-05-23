from django.shortcuts import render, redirect
from contact.models import Contact
from django.core.paginator import Paginator
from contact.form import RegisterForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

def index(request):

    contatos = Contact.objects.all()
    p = Paginator(contatos,8)

    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {
        'page_obj':page_obj,
    }
    return render(
        request,
        'contact/index.html',
        context = context,
    )

def search(request):
    q = request.GET.get('q').strip().lower()
    contatos = Contact.objects.all()
    list_contacts = set()

    for i in contatos:
        if i.name.lower() == q:
            list_contacts.add(i)
        elif i.last_name.lower() == q:
            list_contacts.add(i)
        elif q in str(i.number):
            list_contacts.add(i)
    list_contacts = list(list_contacts)
    p = Paginator(list_contacts,8)

    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {
        'page_obj':page_obj,
        'q':q,
    }
    return render(
        request,
        'contact/index.html',
        context = context,
    )

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request,'Usuário salvo')

            return redirect('contact:index')
        # return redirect('contact:index')
        messages.error(request,'Usuário não salvo')

    context = {
        'form':form,
    }
    return render(
        request,
        'contact/register.html',
        context=context,
    )

def login_view(request):

    form=AuthenticationForm(request)

    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,'Usuário logado')

                return redirect('contact:index')
            
        else:
            messages.error(request,'Login inválido')
            
    context={
        'form':form,
    }
    return render(
        request,
        'contact/login.html',
        context=context,
    )

def logout_view(request):
    logout(request)
    messages.success(request,'Usuário deslogado')
    return redirect('contact:index')

def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Sua senha foi alterada com sucesso!")
            return redirect('contact:login')
        else:
            messages.error(request, "Por favor, coloque uma senha válida")

    context = {
        'form':form,
    }
    return render(
        request,
        'contact/chpassword.html',
        context=context
    )

def delete_user(request):

    confirm = request.POST['confirm']

    if confirm == 'yes':
        usuario = User.objects.get(username=request.user)
        usuario.delete()
        messages.success(request,'Usuário deletado com sucesso')
        return redirect('contact:index')
    
    context={
        'confirm':'yes',
    }

    return render(
        request,
        'contact/login.html',
        context=context,
    )