class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:  # Ensure grades are within a valid range
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100")

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0  # Return 0 if there are no grades

    def __str__(self):
        average = self.get_average_grade()
        return f"Name: {self.name}, Grades: {self.grades}, Average: {average:.2f}"


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_top_students(self):
        # Sort students based on average grade in descending order and return the top 3
        top_students = sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)[:3]
        return top_students

    def get_failed_students(self):
        # Return students with an average grade below 51
        failed_students = [student for student in self.students if student.get_average_grade() < 51]
        return failed_students


# Example Usage
student1 = Student("Alice")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

student2 = Student("Bob")
student2.add_grade(45)
student2.add_grade(50)
student2.add_grade(40)

student3 = Student("Charlie")
student3.add_grade(95)
student3.add_grade(92)
student3.add_grade(89)

student4 = Student("David")
student4.add_grade(60)
student4.add_grade(75)
student4.add_grade(70)

classroom = Classroom()
classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)
classroom.add_student(student4)

# Display top 3 students
print("Top Students:")
for student in classroom.get_top_students():
    print(student)

# Display students who failed
print("\nFailed Students:")
for student in classroom.get_failed_students():
    print(student)
