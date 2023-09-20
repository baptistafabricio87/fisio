from django.db import models
import datetime as dt

# Create your models here.
class Patient(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    address = models.CharField(null=False, blank=False, max_length=255)
    active = models.BooleanField(verbose_name='Ativo', default=True)

    def __str__(self):
        return self.name

HOUR_CHOICES = [(None, '------')] + [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]


class Schedule(models.Model):
    date_schedule = models.DateField(
        auto_created=True, auto_now=False, auto_now_add=False
    )
    time_schedule = models.TimeField(
        auto_created=True, auto_now=False, auto_now_add=False
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Data: {self.date_schedule} | Horario: {self.time_schedule} | Paciente: {self.patient}'
