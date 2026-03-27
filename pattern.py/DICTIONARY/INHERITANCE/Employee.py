class person:
    def greet_person(self):
        print("name: Tharikashree")
class employee(person):
    def greet_employee(self):
        print("salery: 80000")
class manager(employee):
    def greet_manager(self):
        print("department: BME")
m = manager()
m.greet_person()
m.greet_employee()
m.greet_manager()
