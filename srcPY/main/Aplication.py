from srcPY.person.Student import Student
from srcPY.institution.University import University
from srcPY.institution.interlink.Internship import Internship

def main():

    SomeStudent=Student("Dimas")
    SomeStudent1 = Student("Dimas1")
    SomeStudent2 = Student("Dimas2")
    SomeStudent3 = Student("Dimas3")
    SomeStudent4 = Student("Dimas4")
    SomeStudent5 = Student("Dimas5")

    SomeUniver=University("LNU")

    SomeUniver.addStudent(SomeStudent)
    SomeUniver.addStudent(SomeStudent1)
    SomeUniver.addStudent(SomeStudent2)
    SomeUniver.addStudent(SomeStudent3)
    SomeUniver.addStudent(SomeStudent4)
    SomeUniver.addStudent(SomeStudent5)

    SomIntr=Internship("Interlink")


    SomIntr.getStudents(SomeUniver)

if __name__ == '__main__':
    main()
