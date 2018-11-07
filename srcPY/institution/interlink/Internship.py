from srcPY.person.Student import Student
from srcPY.institution.University import University

class Internship():

    def __init__(self,name):
        self.name = name

    def getStudents(self,University):
        counter=0
        for Student in University.S:
            counter += Student.knowledge

        avg=counter/len(University.S)

        for Student in University.S:
            if(Student.knowledge>avg):
                 print(Student.name)


