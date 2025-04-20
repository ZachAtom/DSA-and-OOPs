class Employee:
    Num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, address, pay):
        self.first = first
        self.last = last
        self.address = address
        self.pay = pay
        # Increment the number of employees when a new instance is created
        Employee.Num_of_emps += 1
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.first = first
        self.last = last
    @full_name.deleter
    def full_name(self):
        print("Deleting Name!")
        del self.first
        del self.last
    def apply_raise(self):
         self.pay = int(self.pay * self.raise_amount)
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.address}, {self.pay})"
    def __str__(self):
        return f"Employee: {self.first} {self.last}, Address: {self.address}, Pay: {self.pay}"
emp_1 = Employee("Zach", "Atom", "Thongju", 50000)
emp_2 = Employee("John", "Doe", "Kangpokpi", 50000)
emp_1.full_name = "Lord Zach"
print(emp_1.email)
print(emp_1.first)
print(repr(emp_1))
print(str(emp_1))