

class University:

    def __init__(self, name):
            self.name = name
            self.studentsList = []

    def addStudent(self, student):
        self.studentsList.append(student)
