from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect






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

class viewappointmentlist (ListView):
    model = Appointment
    form_class = ApointmentForm
    template_name = 'dentist/ViewAppointmentList.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class updateappointment (UpdateView):
    model = Appointment
    form_class = UpdateAppointmentForm
    template_name = 'dentist/UpdateAppointment.html'

    def get_success_url(self):
        messages.success(self.request, 'Appointment updated')
        return reverse('viewappointmentlist') 
    #fields = '__all__'
    #fields = ('date', 'doctor_name', 'issue', 'time')

class deleteappointment (DeleteView):
    model = Appointment
    template_name = 'dentist/DeleteAppointment.html'
    success_url = reverse_lazy('viewappointmentlist')
    
    #fields = '__all__'
    #fields = ('date', 'doctor_name', 'issue', 'time')



class createConsultation (CreateView):
    model = Consultation
    form_class = ConsultationForm2
    template_name = 'dentist/CreateConsultation.html'

class viewconsultationlist (ListView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'dentist/ViewConsultationList.html'

class ConsultationDetailView(DetailView):
    model = Patient
    template_name = 'dentist/ViewPatient.html'

'''
def createConsultation(request, pk):

    patient = Patient.objects.get(id=pk)
    form = ConsultationForm(initial = {'patient':patient})
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')


    context= {'form': form}
    return render(request, 'dentist/CreateConsultation.html',context)





def patient(request, pk_test):
    patient= Patient.objects.get(id=pk_test)
    #consultation= patient.consultation_set.all()

    context = {'patient': patient}
    return render(request, 'dentist/ViewPatient.html',context)
'''
    

class viewpatientlist (ListView):
    model = Patient
    form_class = PatientSignUpForm
    template_name = 'dentist/ViewPatientList.html'
    #fields = '__all__'
    #fields = ('title', 'body')

'''
def viewpatientlist(request):
    patient= Patient.objects.all()
    
    context= {'patient':patient}
    return render(request, 'dentist/ViewPatientList.html', context)
'''

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'dentist/ViewPatient.html'


class viewdoctorlist (ListView):
    model = Doctor
    form_class = DoctorSignUpForm
    template_name = 'dentist/ViewDoctorList.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'dentist/ViewDoctor.html'



















    


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
         


