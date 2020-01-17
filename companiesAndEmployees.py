from companies import Company
from employees import Employees

# 1. Create two companies, and 5 people who want to work for them.
Dougs_Mountainside_Adventures = Company("Doug's Mountainside Adventures", "100 Patagonia Way, Missoula, MT", "Fitness")

Carolines_App_Shop = Company("Caroline's App Shop", "400 Music Row, Nashville, TN", "Information Technology")

Caroline = Employees("Caroline Brownlee", "CEO", "January 5, 2020")

Doug = Employees("Doug Boomer", "CEO", "January 1, 2020")

Joseph = Employees("Joseph Brownlee", "Adventure Planner", "March 10, 2020")

Hendrix = Employees("Jimi Hendrix", "Junior Developer", "February 14, 2020")

Gates = Employees("Bill Gates", "Senior Web Developer", "January 5, 2020")

# 2. Assign 2 people to be employees of the first company.
Dougs_Mountainside_Adventures.add_employee(Doug)

Dougs_Mountainside_Adventures.add_employee(Joseph)

# 3. Assign 3 people to be employees of the second company.
Carolines_App_Shop.add_employee(Caroline)

Carolines_App_Shop.add_employee(Hendrix)

Carolines_App_Shop.add_employee(Gates)

# 4. Output a report to the terminal the displays a business name, and its employees.
print(f"{Dougs_Mountainside_Adventures.business_name} is in the {Dougs_Mountainside_Adventures.industry} industry and has the following employees: ") 

Dougs_Mountainside_Adventures.list_employees()

print(f"{Carolines_App_Shop.business_name} is in the {Carolines_App_Shop.industry} industry and has the following employees: ") 

Carolines_App_Shop.list_employees()



