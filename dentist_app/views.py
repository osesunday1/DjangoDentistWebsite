from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.views.generic import *
from .forms import ApointmentForm








def home(request):
    return render(request, 'dentist/home.html' )


def about (request):
    return render(request, 'dentist/about.html' )

def services (request):
    return render(request, 'dentist/services.html' )

def pricing (request):
    return render(request, 'dentist/pricing.html' )

class appointment (CreateView):
    model = Appointment
    form_class = ApointmentForm
    template_name = 'dentist/appointment.html'
    #fields = '__all__'
    #fields = ('title', 'body')


def contact(request):
    if request.method == "POST":
        # retrieve data from form
        message_name= request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']


# send an email
        send_mail(
            'message from' + message_name, #subject
            message, #message
            message_email, #from email
            ['graphicgalacticos@gmail.com'],# to Email
        )
        return render(request, 'dentist/contact.html', {'message_name': message_name})
    else:
       return render(request, 'dentist/contact.html' )
        

    """
        send_mail(
            'message from' + message_name, #subject
            message, #message
            'settings.EMAIL_HOST_USER',
            [message_email, 'graphicgalacticos@gmail.com'],# to Email
            fail_silently=False
        )
        return render(request, 'dentist/contact.html', {'message_name': message_name})
        """
         


