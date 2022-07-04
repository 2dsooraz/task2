"""hospital_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from hospital import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('doctorclick', views.doctorclick_view),
    path('receptionistclick', views.receptionistclick_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('receptionistsignup', views.reception_signup_view),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('receptionistlogin', LoginView.as_view(template_name='hospital/receptionistlogin.html')),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('receptionist-dashboard', views.receptionist_dashboard_view,name='receptionist-dashboard'),
    path('receptionist-book-appointment',views.receptionist_book_appointment_view,name='receptionist-book-appointment'),
    path('receptionist-appointment',views.receptionist_appointment_view,name='receptionist-appointment'),
    path('receptionist-view-doctor', views.receptionist_view_doctor_view,name='receptionist-view-doctor-view'),
    path('receptionist-view-appointment', views.receptionist_view_appointment_view,name='receptionist-view-appointment-view')

]
