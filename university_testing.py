#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing the classes created
"""

__author__ = 'Mohamed Ouertani'

from university_classes import Student,Subject

def test_function():
    """Testing the average and ungraded methods"""

    #Creating student objects
    student1 = Student("Jane","Mary",94946441,"blabla@gmail.com",2021)
    student2 = Student("Parker","Peter",49498444,'whatever@gmail.com',2020)

    #Creating subject objects
    subject1 = Subject("Maths")
    subject2 = Subject("Computer Science")

    #Adding subjects and grades to student object
    student1.add_subject(subject1)
    student1.add_grade(subject1,15)
    student1.add_subject(subject2)
    student1.add_grade(subject2,17)

    student2.add_subject(subject1)
    student2.add_grade(subject1,10)
    student2.add_subject(subject2)
    student2.add_grade(subject2,9)

    #Testing addition of non Subject objects to Student object
    student1.add_subject(1)
    student1.add_grade("whatever",2)


    #Average grades for student object
    print(student1.average_grades())
    print(student2.average_grades())

    #Average grades for subject object
    print(subject1.subject_average())
    print(subject2.subject_average())

    #Ungraded subjects for student object
    subject3 = Subject("Physics")
    student1.add_subject(subject3)
    subject4 = Subject("INLO")
    student2.add_subject(subject4)
    print(student1.ungraded_subjects())
    print(student2.ungraded_subjects())



if __name__ == "__main__":
    test_function()
