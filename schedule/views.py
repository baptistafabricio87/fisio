from rest_framework.viewsets import ModelViewSet
from schedule.models import Patient, Schedule
from schedule.serializers import PatientSerializer, ScheduleSerializer


# Create your views here.
class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
