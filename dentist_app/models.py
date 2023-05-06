from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_scheduler = models.BooleanField(default=False)



class Patient (models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=130)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name

SPECIALTY = [ 
    ('Periodontists','Periodontists' ),
    ('Prosthodontists','Prosthodontists' ),
    ('Pediatric','Pediatric' ),
    ('General Checkup','General Checkup' ),
    ('Toothache','Toothache' ),
    ]

class Doctor (models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=130)
    specialty = models.CharField(choices=SPECIALTY,max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.first_name
    

class Scheduler (models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.TextField(max_length=130)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class Appointment(models.Model):
    ISSUES = [ 
    ('Whitening','Whitening' ),
    ('Toothache','Toothache' ),
    ]
    TIME = [ 
    ('08 AM to 09 AM','08 AM to 09 AM' ),
    ('09 AM to 10 AM','09 AM to 10 AM' ),
    ('10 AM to 11 AM','10 AM to 11 AM' ),
    ('11 AM to 12 PM','11 AM to 12 PM' ),
    ('12 PM to 01 PM','12 PM to 01 PM' ),
    ('01 PM to 02 PM','01 PM to 02 PM' ),
    ('03 PM to 03 PM','02 PM to 03 PM' ),
    ('04 PM to 05 PM','04 PM to 05 PM' ),
    ]
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True )
    date = models.DateTimeField('Appointment Date')
    doctor_name = models.ForeignKey(Doctor, null=True, blank= True, on_delete= models.SET_NULL)
    issue= models.CharField(choices=ISSUES,max_length=120, null= True, blank= True)
    time= models.CharField(choices=TIME,max_length=120, null= True, blank= True)


    def __str__(self):
        return self.patient_name
    

class Sessions(models.Model):
    doctor_name = models.ForeignKey(Doctor, null=True, on_delete= models.SET_NULL)
    patient_name = models.ForeignKey(Patient, null=True, on_delete= models.SET_NULL)
    doctor_comment= models.TextField(max_length=300)
    doctor_recommendation= models.TextField(max_length=300)
    sales_date= models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return self.doctor_name



