from django.shortcuts import render, redirect
from contact.models import Contact
from contact.form import ContactForm
from django.contrib import messages

def add(request):
    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
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
    # print(type(contato.image))
    # contato.image = contato.resize_img(contato.image)
    # print(type(contato.image))
    # out.show()
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
        form = ContactForm(request.POST, request.FILES, instance=contato)

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