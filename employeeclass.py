class Employee:
    def __init__(self, first, last, address):
        self.first = first
        self.last = last
        self.address = address
    def full_name(self):
        return f"{self.first} {self.last}"
        

emp_1 = Employee("Zach", "Atom", "Thongju")
emp_2 = Employee("John", "Doe", "Kangpokpi")
print(emp_1.full_name())    
