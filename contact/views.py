from django.shortcuts import render, redirect
from django.core.mail import send_mail

from contact.forms import ContactForm


def contact_form(request):
    return render(request, 'contact/form.html', {
        'form': ContactForm(),
    })


def contact_processor(request):
    if request.method != "POST":
        return redirect("contact:form")

    form = ContactForm(request.POST)
    if not form.is_valid():
        return redirect("contact:form")

    send_mail(form.cleaned_data['subject'], form.cleaned_data['message'],
            form.cleaned_data['sender'], ['codemash@example.com'])

    return render(request, 'contact/thanks.html', {
        'form': form,
    })
