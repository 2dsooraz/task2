from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

departments=[('Physician','Physician'),
('Dermatologists','Dermatologists'),
('Cardiologist','Cardiologist')
]

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Physician')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Receptionist(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    disease = models.CharField(max_length=100,null=False)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id

class PatientDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctor=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    disease = models.CharField(max_length=100,null=True)
    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    totalFee=models.PositiveIntegerField(null=False)


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)


