'''
Created on Jun 24, 2016

@author: Waqas Ali
'''

class Student(object):
    def __init__(self, Id, FirstName, LastName, Age, Gender, ClassId):
        self._Id = Id
        self._FirstName = FirstName
        self._LastName = LastName
        self._Age = Age
        self._Gender = Gender
        self._ClassId = ClassId        