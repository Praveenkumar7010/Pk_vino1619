#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
def sort_students(students: list[Student]) -> list[Student]:
  """Sorts a list of student objects based on their CGPA in descending order.

  Args:
    students: A list of student objects.

  Returns:
    A list of student objects sorted by CGPA in descending order.
  """

  # Sort the list of student objects using the sorted() function with a lambda key function.
  # The lambda key function compares the CGPA of two student objects and returns the larger CGPA.

  sorted_students = sorted(students, key=lambda student: student.cgpa, reverse=True)

  return sorted_students


class Student:
  def __init__(self, name: str, roll_number: str, cgpa: float):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

# Create a list of student objects.

students = [
    Student("Alice", "1234567890", 9.5),
    Student("Bob", "9876543210", 9.0),
    Student("Carol", "0987654321", 8.5),
]

# Sort the list of student objects by CGPA in descending order.

sorted_students = sort_students(students)

# Print the sorted list of student objects.

for student in sorted_students:
  print(f"{student.name} ({student.roll_number}): {student.cgpa}")


'''
Alice (1234567890): 9.5
Bob (9876543210): 9.0
Carol (0987654321): 8.5
'''
