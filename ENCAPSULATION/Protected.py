class employee:
    def __init__(self, name, salery):
        self._name = name
        self._salery = salery
emp = employee("Tharikashree", 500000)
print(emp._salery)
class manager(employee):
    def show_salery(self):
        print(f"salery:{self._salery}")
mgr = manager("Tharikashree", 500000)
mgr.show_salery()

