class student:
    def __init__(self, name, marks):
        self.name = name
        self.mark = marks
stu = student("Tharika", 95)
print(stu.name)
print(stu.mark)
stu.name = "Thari"
print(stu.name)
