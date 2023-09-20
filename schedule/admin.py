from django.contrib import admin

from .models import Patient, Schedule

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
    ]
    ordering = [
        'name',
    ]


class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'date_schedule',
        'time_schedule',
    ]
    ordering = [
        'date_schedule',
    ]


admin.site.register(Patient)
admin.site.register(Schedule)
