from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dentist_app.urls')),
    path('members/', include('django.contrib.auth.urls')),  
    path('members/', include('members_app.urls')),

] 
