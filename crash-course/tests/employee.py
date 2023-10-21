class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.name = first_name.title()
        self.last_name = last_name.title()
        self.salary = annual_salary

    def give_raise(self, amount=5000):
        self.salary += amount
