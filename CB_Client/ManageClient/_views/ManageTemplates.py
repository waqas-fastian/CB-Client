'''
Created on Jun 24, 2016

@author: Waqas Ali
'''

from django.template.loader import get_template
from django.http.response import HttpResponse

def AddStudentTemplate(request):
    return HttpResponse(get_template('AddStudent.html').render())

def ShowAllStudentsTemplate(request):
    return HttpResponse(get_template('ShowAllStudents.html').render())