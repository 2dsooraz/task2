from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from hospital import models
#from hospital_management.hospital.models import PatientDetails
#from hospital_management.hospital.models import Receptionist
from . import forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test


def home_view(request):
    return render(request,'./hospital/index.html')



def doctorclick_view(request):
    return render(request,'./hospital/doctorclick.html')


def receptionistclick_view(request):
    return render(request,'./hospital/receptionistclick.html')


def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'hospital/doctorsignup.html',context=mydict)


def reception_signup_view(request):
    userForm=forms.ReceptionistUserForm()
    receptionistForm=forms.ReceptionistForm()
    mydict={'userForm':userForm,'receptionistForm':receptionistForm}
    if request.method=='POST':
        userForm=forms.ReceptionistUserForm(request.POST)
        receptionistForm=forms.ReceptionistForm(request.POST,request.FILES)
        if userForm.is_valid() and receptionistForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            receptionist=receptionistForm.save(commit=False)
            receptionist.user=user
            #receptionist.assignedDoctorId=request.POST.get('assignedDoctorId')
            receptionist=receptionist.save()
            my_receptionist_group = Group.objects.get_or_create(name='RECEPTIONIST')
            my_receptionist_group[0].user_set.add(user)
        return HttpResponseRedirect('receptionistlogin')
    return render(request,'hospital/receptionistsignup.html',context=mydict)



def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_receptionist(user):
    return user.groups.filter(name='RECEPTIONIST').exists()



def afterlogin_view(request):
    if is_doctor(request.user):
            return redirect('doctor-dashboard')
    if is_receptionist(request.user):
            return redirect('receptionist-dashboard')


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    appointments=models.Appointment.objects.all().filter(doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.PatientDetails.objects.all().filter(id=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'appointments':appointments,
    }
    return render(request,'hospital/doctor_dashboard.html',context=mydict)     


@login_required(login_url='receptionistlogin')
@user_passes_test(is_receptionist)
def receptionist_dashboard_view(request):
    if request.method == 'POST':
        return HttpResponseRedirect('receptionist-book-appointment')
    return render(request,'hospital/receptionist_dashboard.html')
    


@login_required(login_url='receptionistlogin')
@user_passes_test(is_receptionist)
def receptionist_book_appointment_view(request):
    appointmentForm=forms.AppointmentForm()
    patient=models.PatientDetails.objects.all()
    message=None
    mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            
            #doctor=models.Doctor.objects.get(user_id=request.POST.get('doctorId'))
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.user.id 
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctor')).first_name
            appointment.patientName=request.POST.get('patientNames')
            appointment.description=request.POST.get('description')
            appointment.status=True
            appointment.save(commiit=False)
    return render(request,'hospital/receptionist_book_appointment.html',context=mydict)

@login_required(login_url='receptionistlogin')
@user_passes_test(is_receptionist)
def receptionist_appointment_view(request):
    patient=models.PatientDetails.objects.all()
    return render(request,'hospital/receptionist_appointment.html',{'patient':patient})

@login_required(login_url='receptionistlogin')
@user_passes_test(is_receptionist)
def receptionist_view_appointment_view(request):
    patient=models.PatientDetails.objects.all()   
    appointments=models.Appointment.objects.all()
    return render(request,'hospital/receptionist_view_appointment.html',{'appointments':appointments,'patient':patient})

def receptionist_view_doctor_view(request):
    doctors=models.Doctor.objects.all()
    patient=models.PatientDetails.objects.all() 
    return render(request,'hospital/receptionist_view_doctor.html',{'patient':patient,'doctors':doctors})




