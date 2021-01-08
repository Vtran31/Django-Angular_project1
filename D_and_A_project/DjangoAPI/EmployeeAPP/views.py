from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.fields import NullBooleanField
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeAPP.models import Departments, Employees
from EmployeeAPP.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    #check for GET method
    if request.method == "GET": 
        if id >  0 :
            departments = Departments.objects.filter(DepartmentId = id)
        else:
            departments = Departments.objects.all()
        department_serializer   = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)

    # POST method
    elif request.method == 'POST':
        # get data from request and parse as Json format
        department_data         = JSONParser().parse(request)
        department_serializer   = DepartmentSerializer(data=department_data)

        #check if data is valid
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Add successfuly ", safe=False)
        return JsonResponse("Failed to add", safe=False)

    # PUT method ( update an existing records )
    elif request.method == "PUT": 
        department_data         = JSONParser().parse(request)
        # locate the data in database using "id"
        department              = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serializer   = DepartmentSerializer(department, data=department_data)

        #check if data is valid
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Edited successfuly ", safe=False)
        return JsonResponse("Failed to edit", safe=False)

    elif request.method == "DELETE":

        try:
            if id > 0 :
                department  = Departments.objects.get(DepartmentId = id)
            elif id == 0 :
                department_data = JSONParser().parse(request)
                department  = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
            else : 
                return JsonResponse("Unknow error at Delete", safe=False)

            department.delete()

            return JsonResponse("Delete Successful", safe=False)
        except:
            return JsonResponse("DElete Error", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    #check for GET method
    if request.method == "GET": 
        if id >  0 :
            employee = Employees.objects.filter(EmployeesId = id)
        else:
            employee = Employees.objects.all()
        employee_serializer   = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)

    # POST method
    elif request.method == 'POST':
        # get data from request and parse as Json format
        employee_data         = JSONParser().parse(request)
        employee_serializer   = EmployeeSerializer(data=employee_data)

        #check if data is valid
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Add successfuly ", safe=False)
        return JsonResponse("Failed to add", safe=False)

    # PUT method ( update an existing records )
    elif request.method == "PUT": 
        employee_data         = JSONParser().parse(request)
        # locate the data in database using "EmployeesId" from API <<<<-----
        employee              = Employees.objects.get(EmployeesId = employee_data['EmployeesId'])
        employee_serializer   = EmployeeSerializer(employee, data=employee_data)

        #check if data is valid
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Edited successfuly ", safe=False)
        return JsonResponse("Failed to edit", safe=False)

    elif request.method == "DELETE":

        try:
            if id > 0 :
                employee  = Employees.objects.get(EmployeesId = id)
            elif id == 0 :
                employee_data = JSONParser().parse(request)
                employee  = Employees.objects.get(EmployeesId = employee_data['EmployeesId'])
            else : 
                return JsonResponse("Unknow error at Delete", safe=False)

            employee.delete()

            return JsonResponse("Delete Successful", safe=False)
        except:
            return JsonResponse("DElete Error", safe=False)


@csrf_exempt
def SaveFile(request): 
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    
    return JsonResponse(file_name, safe=False)