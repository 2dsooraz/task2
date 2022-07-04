from django.contrib import admin
from .models import Doctor,Receptionist,Appointment,PatientDetails
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Receptionist, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDetails, PatientDetailsAdmin)
