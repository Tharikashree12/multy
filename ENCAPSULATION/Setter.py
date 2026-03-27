class student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")
stu = student("Tharikashree", 88)
stu.set_marks(105)
stu.set_marks(90)
print(stu.get_marks())
