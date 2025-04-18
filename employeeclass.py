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
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
import datetime
my_date = datetime.date(2023, 10, 9)
print(Employee.is_workday(my_date))        
print(Employee.Num_of_emps)
emp_1 = Employee("Zach", "Atom", "Thongju", 50000)
emp_2 = Employee("John", "Doe", "Kangpokpi", 50000)
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)