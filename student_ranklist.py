from abc import ABC, abstractmethod
from copy import copy, deepcopy


# Abstract Class
class Evaluation(ABC):

    @abstractmethod
    def calculate_grade(self):
        pass


# Base Class
class Person:
    def __init__(self, name, age):
        self.__name = name       # Private attribute
        self.__age = age         # Private attribute

    # Getter methods - Encapsulation
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Derived Class
class Student(Person, Evaluation):

    student_count = 0

    def __init__(self, name, age, roll_number, marks):
        super().__init__(name, age)

        self.roll_number = roll_number
        self.marks = marks

        Student.student_count += 1

    # Calculate total marks
    def calculate_total(self):
        return sum(self.marks)

    # Calculate average
    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    # Abstract method implementation
    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    # Display student details
    def display(self):
        print("Name        :", self.get_name())
        print("Age         :", self.get_age())
        print("Roll Number :", self.roll_number)
        print("Marks       :", self.marks)
        print("Total       :", self.calculate_total())
        print("Average     :", round(self.calculate_average(), 2))
        print("Grade       :", self.calculate_grade())

    # Operator Overloading
    def __lt__(self, other):
        return self.calculate_total() < other.calculate_total()

    # Static method
    @staticmethod
    def validate_marks(marks):
        return 0 <= marks <= 100

    # Class method
    @classmethod
    def display_student_count(cls):
        print("\nTotal Number of Students:", cls.student_count)


# Sports Class
class Sports:

    def __init__(self, sports_score=0):
        self.sports_score = sports_score

    def display_sports_score(self):
        print("Sports Score:", self.sports_score)


# Multiple Inheritance
class Result(Student, Sports):

    def __init__(self, name, age, roll_number, marks, sports_score=0):
        Student.__init__(self, name, age, roll_number, marks)
        Sports.__init__(self, sports_score)

    # Polymorphism - overriding display()
    def display(self):
        super().display()
        self.display_sports_score()

    def final_score(self):
        return self.calculate_total() + self.sports_score


# Main Program

students = []

try:
    n = int(input("Enter number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be greater than 0.")

    for i in range(n):

        print(f"\nEnter details for Student {i + 1}")

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        roll_number = int(input("Enter Roll Number: "))

        marks = []

        for j in range(3):
            while True:
                mark = int(input(f"Enter marks for Subject {j + 1}: "))

                if Student.validate_marks(mark):
                    marks.append(mark)
                    break
                else:
                    print("Invalid marks! Enter marks between 0 and 100.")

        sports_score = int(input("Enter Sports Score: "))

        student = Result(
            name,
            age,
            roll_number,
            marks,
            sports_score
        )

        students.append(student)

    # Display original student details
    print("\n" + "=" * 50)
    print("STUDENT DETAILS")
    print("=" * 50)

    for student in students:
        student.display()
        print("-" * 50)

    # Shallow Copy
    shallow_copy = copy(students)

    # Deep Copy
    deep_copy = deepcopy(students)

    # Sort using overloaded __lt__
    students.sort()

    # Reverse to get highest marks first
    students.reverse()

    # Display Rank List
    print("\n" + "=" * 60)
    print("STUDENT RANK LIST")
    print("=" * 60)

    rank = 1

    for student in students:
        print(
            f"Rank: {rank} | "
            f"Name: {student.get_name()} | "
            f"Roll No: {student.roll_number} | "
            f"Total: {student.calculate_total()} | "
            f"Average: {student.calculate_average():.2f} | "
            f"Grade: {student.calculate_grade()} | "
            f"Sports: {student.sports_score}"
        )

        rank += 1

    # Optional final score including sports
    print("\n" + "=" * 60)
    print("FINAL SCORE INCLUDING SPORTS")
    print("=" * 60)

    for student in students:
        print(
            student.get_name(),
            "=> Academic Total:",
            student.calculate_total(),
            "+ Sports:",
            student.sports_score,
            "= Final Score:",
            student.final_score()
        )

    # Class Method
    Student.display_student_count()

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)


