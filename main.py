from prettytable import PrettyTable
import sys

class Teacher():
    def teacher_information_input(self):
        self.name        = str(input("Enter teacher's name: "))
        self.surname     = str(input("Enter teacher's surname: "))
        self.patronymics = str(input("Enter teacher's patronymics: "))
        self.age         = float(input("Enter teacher's age: "))
        self.rank        = str(input("Enter teacher's rank: "))
        self.gender      = str(input("Enter teacher's gender: "))

    def show_teacher_information():
        print("Name:        " + self.name)
        print("Surname:     " + self.surname)
        print("Patronymics: " + self.patronymics)
        print("Age:         " + self.age)
        print("Rank:        " + self.rank)
        print("Gender:      " + self.gender)

    def add_teacher_information():
        pass

    def delete_teacher_information():
        pass

    def teacher_salary():
        pass

class Student():
    def student_information_input():
        self.sname       = str(input("Enter student's name: "))
        self.surname     = str(input("Enter student's surname: "))
        self.patronymics = str(input("Enter student's patronymics: "))
        self.age         = float(input("Enter student's age: "))
        self.study_year  = int(input("Enter student's studying year: "))
        self.gender      = str(input("Etner student's gender: "))

    def show_student_information():
        print("Name:        " + self.name)
        print("Surname:     " + self.surname)
        print("Patronymics: " + self.patronymics)
        print("Age:         " + self.age)
        print("Rank:        " + self.rank)
        print("Gender:      " + self.gender)

    def add_student_information():
        pass

    def delete_student_information():
        pass

if __name__ == '__main__':
    t = Teacher()
    s = Student()
    
    while(True):
        print("-------------------------------")
        print("Input:\n  Sign up\n  Sign in\n  Exit")

        choice = str(input("Choice:  "))
        if choice.:
            if choice == "exit" or "Exit":
                sys.exit()

            elif choice == "sign up" or "Sign up":
                print("Student | Teacher: ")
                pos_input = str(input("Position: "))
                if pos_input == "teacher" or "Teacher":
                    t.teacher_information_input()
                elif pos_input == "student" or "Student":
                    s.student_information_input()
            
            elif choice == "sign in" or "Sign in":
                print("Student | Teacher: ")
                pos_input = str(input("Position: "))
                if pos_input == "teacher" or "Teacher":
                    t.show_teacher_information()
                elif pos_input == "student" or "Student":
                    s.show_student_information()