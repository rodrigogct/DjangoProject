import email
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = f'Message from {contact_form.cleaned_data["name"]}'
            message = contact_form.cleaned_data["message"]
            sender = contact_form.cleaned_data["email"]
            recipients = ["rodrigogcdt@gmail.com"]
            try: 
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse ('Invalid header found')
            return redirect("/contact/?valid")

            # return redirect("/contact/?valid")
    return render(request, "contact.html", {'myForm': contact_form})