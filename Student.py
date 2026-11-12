class Student:
    def __init__(self, name, age, student_id, gpa):
        self.__name = name
        self.__age = age
        self.__student_id = student_id
        self.__gpa= gpa
        self.__clubs=set()
        self.__active=True

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def add_club(self, club):
        self.__clubs.add(club)

    def set_active(self, active):
        self.__active = active

    def get_details(self):
        return f"Name: {self.__name}, Age: {self.__age}, Student ID: {self.__student_id}, GPA: {self.__gpa}, Clubs: {', '.join(self.__clubs)}, Active: {self.__active}"

    def print_details(self):
        print(self.get_details())

