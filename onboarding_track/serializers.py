from rest_framework import serializers
from onboarding_track.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')
        
        
class EmployeeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'       
