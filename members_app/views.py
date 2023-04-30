from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages
from dentist_app.models import *
from dentist_app.forms import PatientSignUpForm
from django.http import HttpResponseRedirect


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user )
            return redirect ('home')
        else:
            messages.success(request, ("there was an error logging in"))
            return redirect ('login') 
    else:
        return render(request, 'authenticate/login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logged Out"))
    return redirect ('home')




class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'dentist/signupPatient.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

