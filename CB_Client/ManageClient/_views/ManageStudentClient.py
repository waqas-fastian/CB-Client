'''
Created on Jun 24, 2016

@author: Waqas Ali
'''

import ManageCB.views
from ManageClient.customClasses.Student import Student
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def AddStudent(request):
    FirstName = request.POST.get('FirstName')
    LastName = request.POST.get('LastName')
    Age = request.POST.get('Age')
    Gender = request.POST.get('Gender')
    ClassId = request.POST.get('ClassId')
    newStudent = Student(0, FirstName, LastName, Age, Gender, ClassId)
    res = ManageCB.views.AddNewStudent(newStudent)
    return HttpResponse(res)
