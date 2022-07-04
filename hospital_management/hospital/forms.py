from django import forms
from django.contrib.auth.models import User
from . import models

class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department']

class ReceptionistUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class ReceptionistForm(forms.ModelForm):
    #assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Receptionist
        fields=['address','mobile']

class PatientForm(forms.ModelForm):
    #doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.PatientDetails
        fields=['address', 'admitDate', 'assignedDoctor', 'disease', 'mobile', 'patientName', 'releaseDate', 'totalFee']


class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    #patientId=forms.ModelChoiceField(queryset=models.PatientDetails.objects.all().filter(status=True),empty_label="Patient Name and Symptoms")
    class Meta:
        model=models.Appointment
        fields=['description','doctorName','patientName','doctorId','patientId']


        