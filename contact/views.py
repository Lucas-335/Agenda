from django.shortcuts import render, redirect
from contact.models import Contact
from django.core.paginator import Paginator
from contact.form import ContactForm
from django.urls import reverse
# Create your views here.

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
        elif q in i.number:
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

def add(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect("contact:index")
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(
        request,
        'contact/add.html',
        context=context
        )

def single_contact(request, num):
    
    contato = Contact.objects.get(id__exact=num)
    context = {
            'contato':contato,
            }
    return render(
        request,
        'contact/sgcontact.html',
        context=context,
        )

def delete(request,num):
    
    confirmation = request.POST.get('confirmation')
    
    if confirmation == 'no':

        contato = Contact.objects.get(id__exact=num)
        context= {
            'contato':contato,
            'confirmation':'yes'
        }
        # contato.delete()
        # return redirect("contact:delete", num)
        return render(request,'contact/sgcontact.html',context=context)
    else:
        contato = Contact.objects.get(id__exact=num)
        contato.delete()
        return redirect('contact:index')
    
def edit(request, num):

    contato = Contact.objects.get(id__exact=num)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contato)

        if form.is_valid():
            form.save()
            return redirect('contact:index')

    form = ContactForm(instance=contato)
    context = {
        'contato':contato,
        'form':form,
    }
    return render(
        request,
        'contact/edit.html',
        context=context

    )