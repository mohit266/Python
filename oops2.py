class Employee:

    # Constructor
    def __init__(self, e_name, e_salary, e_role):
        self.name = e_name
        self.salary = e_salary
        self.role = e_role

    def print_details(self):
        return f"The Name is {self.name}, Salary is {self.salary} and role is {self.role}"

Mohit = Employee("Mohit", 23000, "Instructor")

print(Mohit.print_details())
