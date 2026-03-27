class technical:
    def coding(self):
        print("skill: coding in python")
class nontechnical:
    def management(self):
        print("skill: project management")
class employee(technical, nontechnical):
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(f"employee name: {self.name}")
emp = employee("Tharikashree")
emp.show_name()
emp.coding()
emp.management()

