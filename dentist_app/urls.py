from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('pricing.html', views.pricing, name="pricing"),

    #path('createconsultation', views.createConsultation, name= "createconsultation"),
    path ('createconsultation/create/<int:pk>', createConsultation.as_view(), name= 'createconsultation'),
    path ('viewconsultationlist', viewconsultationlist.as_view(), name= 'viewconsultationlist'),
    #path ('consultationview/<int:pk>', ConsultationDetailView.as_view(), name='consultationview' ),

    path ('appointment', appointment.as_view(), name= 'appointment'),
    path ('viewappointmentlist', viewappointmentlist.as_view(), name= 'viewappointmentlist'),
    path ('viewpatientlist', viewpatientlist.as_view(), name= 'viewpatientlist'),
    path ('viewdoctorlist', viewdoctorlist.as_view(), name= 'viewdoctorlist'),
    #path ('viewpatientlist', views.viewpatientlist, name= 'viewpatientlist'),
    path ('appointment/update/<int:pk>', updateappointment.as_view(), name='updateappointment' ),
    path ('appointment/<int:pk>/delete', deleteappointment.as_view(), name='deleteappointment' ),

    #path ('patient/<str:pk_test>/', views.patient, name="patient"),
    path ('patientview/<int:pk>', PatientDetailView.as_view(), name='patientview' ),
    path ('doctorview/<int:pk>', DoctorDetailView.as_view(), name='doctorview' ),
    
]
