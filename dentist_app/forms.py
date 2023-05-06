from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *
from django.forms import ModelForm



class PatientSignUpForm(UserCreationForm):  
    first_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True, widget = forms.EmailInput(attrs={'class':'form-control'}))
    address = forms.CharField(required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2','first_name', 'last_name', 'phone', 'email', 'address')
    @transaction.atomic
    def save(self):
        
        user = super().save(commit=False)
        
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.first_name=self.cleaned_data.get('first_name')
        patient.last_name=self.cleaned_data.get('last_name')
        patient.phone=self.cleaned_data.get('phone')
        patient.email=self.cleaned_data.get('email')
        patient.address=self.cleaned_data.get('address')
        patient.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(PatientSignUpForm, self). __init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




SPECIALTY = [ 
    ('Periodontists','Periodontists' ),
    ('Prosthodontists','Prosthodontists' ),
    ('Pediatric','Pediatric' ),
    ('General Checkup','General Checkup' ),
    ('Toothache','Toothache' ),
    ]





class DoctorSignUpForm(UserCreationForm):  
    first_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True, widget = forms.EmailInput(attrs={'class':'form-control'}))
    specialty = forms.CharField(required=False, widget=forms.Select(choices=SPECIALTY, attrs={'class':'form-control'}))
    address = forms.CharField(required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta(UserCreationForm.Meta):
        model = User
        #fields = ('username', 'password1', 'password2','first_name', 'last_name', 'phone', 'email', 'specialty','address')
    @transaction.atomic
    def save(self):
        
        user = super().save(commit=False)
        
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.first_name=self.cleaned_data.get('first_name')
        doctor.last_name=self.cleaned_data.get('last_name')
        doctor.phone=self.cleaned_data.get('phone')
        doctor.email=self.cleaned_data.get('email')
        doctor.specialty=self.cleaned_data.get('specialty')
        doctor.address=self.cleaned_data.get('address')
        doctor.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(DoctorSignUpForm, self). __init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'





class SchedulerSignUpForm(UserCreationForm):  
    first_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True, widget = forms.EmailInput(attrs={'class':'form-control'}))
    address = forms.CharField(required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2','first_name', 'last_name', 'phone', 'email', 'address')
    @transaction.atomic
    def save(self):
        
        user = super().save(commit=False)
        
        user.is_scheduler = True
        user.save()
        scheduler = Scheduler.objects.create(user=user)
        scheduler.first_name=self.cleaned_data.get('first_name')
        scheduler.last_name=self.cleaned_data.get('last_name')
        scheduler.phone=self.cleaned_data.get('phone')
        scheduler.email=self.cleaned_data.get('email')
        scheduler.address=self.cleaned_data.get('address')
        scheduler.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(SchedulerSignUpForm, self). __init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class DateInput(forms.DateInput):
    input_type = 'date'

class ApointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields= ('patient_name', 'date','issue', 'time') 
        widgets= {
            'patient_name': forms.Select(attrs={'class':'form-control', 'value': '', 'id':'elder'}),
            #'patient_name': forms.Select(attrs={'class':'form-control', 'placeholder': 'what is your name'}),
            'date': DateInput(attrs={'type': 'date', 'class':'form-control', 'placeholder': 'Tell us the date'}),
            'issue': forms.Select(attrs={'class':'form-control'}),
            'time': forms.Select(attrs={'class':'form-control'}),
            #'doctor_name': forms.Select(attrs={'class':'form-control', 'type':'hidden'}),
        }
'''
        labels= {
            'patient_name': 'name of patient',
            'date': '',
            'issue':'',
            'doctor_name':'',

        }

'''