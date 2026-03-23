student = {}
def add_student(name, marks):
    student[name] = marks
    print("student added")
def display_student():
    for name, marks in student.items():
        print(name, ":", marks)
add_student("Tharika", 88)
add_student("Priya", 95)
