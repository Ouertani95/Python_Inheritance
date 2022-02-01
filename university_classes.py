#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creating the university organisation with classes
"""

from __future__ import division


__author__ = 'Mohamed Ouertani'



class University:

    """Define University class"""

    def __init__(self,site):
        self.site = site
        self.departments = None

    def get_site(self):
        """get university site"""
        return self.site

    def set_site(self,site):
        """change university site"""
        self.site = site

    def get_departments(self):
        """get university departments"""
        return self.departments

    def add_department(self,department):
        """add new department to university"""
        self.departments.append(department)

    def remove_department(self,department):
        """remove a department from university"""
        if department in self.departments:
            self.departments.remove(department)
            return "Department removed from university"
        return "Department not in university"



class Department:

    """Define department class"""

    def __init__(self,professors,department_head):
        self.professors = professors
        self.department_head = department_head

    def get_professors(self):
        """get list of professors in department"""
        return self.professors

    def add_professor(self,professor):
        """add a professor to the department"""
        self.professors.append(professor)

    def remove_professor(self,professor):
        """remove a professor from the department"""
        if professor in self.professors:
            self.professors.remove(professor)
            return "Professor removed from this department"
        return "Professor not in this department"

    def get_department_head(self):
        """get the head professor of the department"""
        return self.department_head

    def set_department_head(self,professor):
        """change the head professor of the department"""
        if professor in self.professors:
            self.department_head = professor
            return "Professor is made head this department"
        return "Professor not in this department"



class Subject:

    """Define subject class"""

    def __init__(self,name):
        self.name = name
        self.students = []

    def get_name(self):
        """get the subject name"""
        return self.name

    def set_name(self,name):
        """ change the subject name"""
        if name.__class__.__name__ != "str":
            print ("Please provide string object to be change the name")
        else:
            self.name = name

    def get_students(self):
        """get the students assigned to the subject"""
        if len(self.students) == 0:
            return "No students for this subject"
        list_students = []
        for i in self.students:
            list_students.append(i.name+" "+i.surname)
        return f"The students attending this subject are : {list_students}"

    def add_student(self,student):
        """assign a student to the subject"""
        if student.__class__.__name__ != "Student":
            print (f"{student} is not a Student object try again")
        elif student not in self.students:
            student.add_subject(self)
            print(f"""The student {student.name} {student.surname}
                    was successfully assigned to this subject""")
        else:
            print(f"""The student {student.name} {student.surname}
                  is already assigned to this subject""")

    def remove_student(self,student):
        """remove a student from the subject"""
        if student.__class__.__name__ != "Student":
            print (f"{student} is not a Student object try again")
        elif student in self.students:
            self.students.remove(student)
            print("Student removed from this subject")
        else:
            print("Student not in this subject")


    def subject_average(self):
        """get average grades of the subject"""
        sum_grades = 0
        number_subjects = 0
        for i in enumerate(self.students):
            student = i[1]
            for j,k in student.subjects.items():
                if j.get_name() == self.get_name()and k is not None:
                    sum_grades += k
                    number_subjects += 1
        if number_subjects == 0 :
            return "No graded students"
        return f"The average grade of {self.name} is {sum_grades / number_subjects}"



class Person:

    """Define person class"""

    def __init__(self,name,surname,phone_number,email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def set_phone_number(self,phone_number):
        """change phone number of the person"""
        if phone_number.__class__.__name__ != "int":
            print("Please provide integer object to be change the number")
        else:
            self.phone_number = phone_number

    def set_email(self,email):
        """change the email of the person"""
        if email.__class__.__name__ != "str":
            print("Please provide string object to change email")
        else:
            self.email = email

    def print_resume(self):
        """print the resume of the person attributes"""
        print(self.name, self.surname, self.phone_number, self.email)



class Student(Person):

    """Define student class"""

    def __init__(self, name, surname, phone_number, email,entry_year):
        super().__init__(name, surname, phone_number, email)
        self.entry_year = entry_year
        self.subjects = {}

    def get_entry_year(self):
        """get the entry year of the student"""
        return self.entry_year

    def get_subjects(self):
        """get the subjects to which the student is assigned"""
        if len(self.subjects) == 0:
            return f"The student {self.name} {self.surname} is not assigned to any subjects"
        list_subjects = []
        for subject in self.subjects:
            list_subjects.append(subject.get_name())
        return f"The student {self.name} {self.surname} is assigned to : {list_subjects} "

    def add_subject(self,subject,grade=None):
        """add a new subject to the student"""
        if subject.__class__.__name__ == "Subject":
            self.subjects[subject] = grade
            subject.students.append(self)
        else:
            print(f"{subject} is not a Subject object try again")

    def remove_subject(self,subject):
        """remove an assigned subject to the student"""
        if subject.__class__.__name__ != "Subject":
            return "Please provide Subject object to be removed"
        if subject in self.subjects.keys():
            self.subjects.pop(subject)
            return "Subject removed for this student"
        return "Student not in this subject"

    def add_grade(self,subject,grade):
        """add a new grade to an assigned subject for the student"""
        if subject.__class__.__name__ != "Subject":
            print(f"{subject} is not a Subject object try again")
        elif subject in self.subjects.keys():
            self.subjects[subject] = grade
        else:
            print(f"{self.name} {self.surname} is not assigned to subject :  {subject} ")


    def average_grades(self):
        """calcule the average grade of the student"""
        sum_grades = 0
        graded_subjects = 0
        for i in self.subjects.values():
            if i is not None:
                sum_grades += i
                graded_subjects +=1
        if graded_subjects == 0:
            return "No graded subjects"
        return f"The average grade for {self.name} {self.surname} is {sum_grades/graded_subjects}"

    def ungraded_subjects(self):
        """get the ungraded subject names for the student"""
        if None not in self.subjects.values():
            return f"All subjects for {self.name} {self.surname} are graded"
        for i,j in self.subjects.items():
            list_subjects = []
            if j is None:
                list_subjects.append(i.get_name())
        return f"The ungraded subjects for {self.name} {self.surname} are : {list_subjects}"



class Professor(Person):

    """Define professor class"""

    def __init__(self, name, surname, phone_number, email,
                 start_date, salary, subject):
        super().__init__(name, surname, phone_number, email)
        self.start_date = start_date
        self.salary = salary
        self.subject = subject

    def get_start_date(self):
        """get the start date for the professor"""
        return self.start_date

    def get_salary(self):
        """get the salary of the professor"""
        return self.salary

    def set_salary(self,salary):
        """change the salary of the professor"""
        self.salary = salary

    def get_subject(self):
        """get the subject of the professor"""
        return self.subject

    def set_subject(self,subject):
        """change the subject of the professor"""
        self.subject = subject



class Room:

    """Define room class"""

    def __init__(self,room_id,capacity):
        self.room_id = room_id
        self.capacity = capacity

    def get_room_id(self):
        """get the room id"""
        return self.room_id

    def set_room_id(self,room_id):
        """change the room id"""
        self.room_id = room_id

    def get_capacity(self):
        """get the room capacity"""
        return self.capacity

    def set_capacity(self,capacity):
        """change the room capacity"""
        self.capacity = capacity
