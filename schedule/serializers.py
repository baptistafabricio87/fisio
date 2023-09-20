from rest_framework.serializers import HyperlinkedModelSerializer
from schedule.models import Patient, Schedule

# Define representação da API
class PatientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'address', 'active',]
        
class ScheduleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ['date_schedule', 'time_schedule', 'patient']
