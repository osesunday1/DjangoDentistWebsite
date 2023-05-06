from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login', views.login_user, name= 'login' ),
    path('logout', views.logout_user, name= 'logout' ),
    path('signupPatient', PatientSignUpView.as_view(), name='signupPatient'),
    path('signupDoctor', DoctorSignUpView.as_view(), name='signupDoctor'),
    path('signupScheduler', SchedulerSignUpView.as_view(), name='signupScheduler'),
]
