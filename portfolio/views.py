from django.shortcuts import render

from portfolio.forms import ContactForm
from .models import Project
from django.core.mail import send_mail

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Here you can use Django's send_mail function to send an email to yourself with the contact information
            send_mail(
                'Contact Form Submission',
                f'{name} {email} said {message}',
                email,
                ['your-email@example.com'], # Replace with your email
                fail_silently=False,
            )
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})