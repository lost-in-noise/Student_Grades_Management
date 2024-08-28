# Student Grades Management

This project demonstrates a system to manage student grades using Object-Oriented Programming (OOP) principles.

## Classes

### `Student` Class
- **Attributes:**
  - `name`: Student's name.
  - `grades`: List of student's grades.
- **Methods:**
  - `__init__(self, name)`: Initializes `name` and `grades`.
  - `add_grade(self, grade)`: Adds a grade.
  - `get_average_grade(self)`: Returns the average grade.
  - `__str__(self)`: Returns a string representation of the student.

### `Classroom` Class
- **Attributes:**
  - `students`: List of `Student` objects.
- **Methods:**
  - `__init__(self)`: Initializes the `students` list.
  - `add_student(self, student)`: Adds a `Student`.
  - `get_top_students(self)`: Returns the top 3 students by average grade.
  - `get_failed_students(self)`: Returns students with an average grade below 51.

## Usage

1. Create `Student` instances and add grades.
2. Add students to a `Classroom`.
3. Use `get_top_students` and `get_failed_students` to display results.

## Example

```python
student1 = Student("Alice")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

classroom = Classroom()
classroom.add_student(student1)

print("Top Students:", classroom.get_top_students())
print("Failed Students:", classroom.get_failed_students())
```
