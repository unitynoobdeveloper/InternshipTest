from srcPY.person.Student import Student
from srcPY.institution.University import University
from srcPY.institution.interlink.Internship import Internship


def main():

    university = University("LNU")

    university.addStudent(Student("Dmytro"))
    university.addStudent(Student("Dmytro1"))
    university.addStudent(Student("Dmytro2"))
    university.addStudent(Student("Dmytro3"))
    university.addStudent(Student("Dmytro4"))
    university.addStudent(Student("Dmytro5"))
    university.addStudent(Student("Dmytro6"))
    university.addStudent(Student("Dmytro7"))

    internship = Internship("Interlink")
    print("List of internship's students:")
    print(internship.get_students(university))


if __name__ == '__main__':

    main()
