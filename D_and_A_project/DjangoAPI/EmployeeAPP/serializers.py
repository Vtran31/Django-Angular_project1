from django.utils.translation import deactivate
from rest_framework import serializers
from EmployeeAPP.models import Departments, Employees


class DepartmentSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Departments
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employees
        fields = '__all__'

