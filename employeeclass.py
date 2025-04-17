class Employee:
    Num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, address, pay):
        self.first = first
        self.last = last
        self.address = address
        self.pay = pay
        Employee.Num_of_emps += 1
    def full_name(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
         self.pay = int(self.pay * self.raise_amount)
            
print(Employee.Num_of_emps)
emp_1 = Employee("Zach", "Atom", "Thongju", 50000)
emp_2 = Employee("John", "Doe", "Kangpokpi", 50000)
emp_1.raise_amount = 1.05
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.Num_of_emps)