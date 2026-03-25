class Employe:
    company = "Infosys" 
    def __init__(self, name, mark, department, regno):
        self.name = name
        self.mark = mark
        self.department = department
        self.regno = regno
    def display(self):
        print("Name:", self.name)
        print("Mark:", self.mark)
        print("Department:", self.department)
        print("regno:", self.regno)
t1 = Employe(
    "Tharikashree",
    88.8,
    "Biomedical",
    192319056
)

t2 = Employe(
    "Kamali",
    90.1,
    "Biomedical",
    192319063,
)

t3 = Employe(
    "Prithiga",
    90,
    "Biomedical",
    192319062
)

t1.display()
t2.display()
t3.display()
