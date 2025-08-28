from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    """Display contact form and handle submissions"""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email notification
            subject = f'New Contact Form Submission: {contact.subject}'
            message = f'''
            New contact form submission:

            From: {contact.name}
            Email: {contact.email}
            Subject: {contact.subject}

            Message:
            {contact.message}
            '''

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except Exception:
                # Email sending failed, but still save the contact
                pass

            messages.success(
                request,
                'Thank you for your message! We will get back to you soon.'
            )
            return redirect('contact_success')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """Display success page after form submission"""
    return render(request, 'contact/contact_success.html')
