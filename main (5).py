def sort_students(students):
  sorted_students=sorted(students,key=lambda x:x.cgpa,reverse=True)
  return sorted_students

class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

students=[Student("Alice","A001",3.7),Student("Bob","B002",3.9),Student("Charlie","C003",3.5)]

sorted_students=sort_students(students)
for student in sorted_students:
  print(student.name,student.roll_number,student.cgpa)