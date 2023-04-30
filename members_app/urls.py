from django.urls import path
from . import views
from .views import PatientSignUpView

urlpatterns = [
    path('login', views.login_user, name= 'login' ),
    path('logout', views.logout_user, name= 'logout' ),
    path('signupPatient', PatientSignUpView.as_view(), name='signupPatient'),
]
