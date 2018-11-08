
class Internship:

    def __init__(self, name):
        self.name = name
        self.list_of_internships = ""
        self.avg = 0.0

    def get_students(self, university):

        sum_counter = 0

        for student in university.studentsList:
            sum_counter += student.knowledge

        self.avg = sum_counter/len(university.studentsList)

        for student in university.studentsList:
            if(student.knowledge > self.avg):
                self.list_of_internships += student.name+"\n"

        return self.list_of_internships

