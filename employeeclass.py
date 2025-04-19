class Employee:
    Num_of_emps = 0
    raise_amount = 1.10
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
class Developer(Employee):
    raise_amount = 1.20
    def __init__(self, first, last, address, pay, prog_lang):
        super().__init__(first, last, address, pay)
        self.prog_lang =  prog_lang

class Manager(Employee):
    raise_amount = 1.15
    def __init__(self, first, last, address, pay, employees=None):
        super().__init__(first, last, address, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.full_name())
dev_1 = Developer("Zach", "Atom", "Thongju", 50000, "Python")
dev_2 = Developer("John", "Doe", "Kangpokpi", 50000, "Java")
mgr_1 = Manager("Luke", "Skywalker", "Delhi", 60000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
