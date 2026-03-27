class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"name: {self.name}, age:{self.age}")
class employee(person):
    def __init__(self, name, age, salery):
        super().__init__(name, age)
        self.salery = salery
    def show_employee_info(self):
        print(f"name:{self.name},age:{self.age}, salery:{self.salery}")
emp = employee("Tharikashree", 20, 50000)
emp.show_info()
emp.show_employee_info()
                        