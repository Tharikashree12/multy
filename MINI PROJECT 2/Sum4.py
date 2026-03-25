class student:
    def __init__(self, name, regno, marks, branch, address, contact):
        self.name = name
        self.regno = regno
        self.marks = marks
        self.branch = branch
        self.address = address
        self.contact = contact
    def display(self):
            print("Name:", self.name)
            print("Regno:", self.regno)
            print("Branch:", self.branch)
            print("Marks:", self.marks)
            print("Address:", self.address)
            print("Contact:", self.contact)

s1 = student(
   "Tharikashree",
    192319056,
    88,
    "BME",
    "Chennai",
    8668142308
) 

s2 = student(
    "Kamali",
    192319063,
    90,
    "BME",
    "Chennai",
    6381232921
)

s3 = student(
    "Prithiga",
    192319062,
    85,
    "BME",
    "Chennai",
    6383447933
)

s1.display()
s2.display()
s3.display()

