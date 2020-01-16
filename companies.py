# Create a Company type that employees can work for. A company should have a business name, address, and industry type.

class Company:

    def __init__(self, business_name, address, industry):
        self.business_name = business_name
        self.address = address
        self.industry = industry
        self.employees = list()

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(employee.name)
