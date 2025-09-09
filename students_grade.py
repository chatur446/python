#grades of student
student_grade = int(input("marks: "))
if (student_grade >= 90):
    print("Student is in grade A")
elif (student_grade >= 80 and student_grade < 90):
    print("Student is in grade B")
elif (student_grade >= 70 and student_grade < 80):
    print("student is in grade C")
else:
    print("student is in grade D")  
