from urbanPlanner import Building
from city import City

# For this exercise, all the logic of constructing buildings and building your city will be in main.py, so take all of your logic from urbanPlanner.py and move it over to main.

# LESSONS CARRIED OVER FROM urbanPlanner.py for URBAN PLANNER TWO EXERCISE:

# 4. Create 5 building instances
Empire_State_Building = Building("Empire State Building", "500 Empire State Blvd.", 102)

Tutor_Style_Home = Building("Tutor Style Home", "100 Williamsburg Ave.", 2)
Cape_Cod_Style_Home = Building("Cape Cod Style Home", "349 Walter Bridge Rd.", 2)
Mansion_Style_Home = Building("Mansion Style Home", "293 Island St.", 3)
Flat_Apartment = Building("Flat Apartment", "852 Main St.", 1)

# 5. Have each one get purchased by a real estate magnate
Empire_State_Building.purchase("Caroline Brownlee")
Tutor_Style_Home.purchase("Caroline Brownlee")
Cape_Cod_Style_Home.purchase("Caroline Brownlee")
Mansion_Style_Home.purchase("Caroline Brownlee")
Flat_Apartment.purchase("Caroline Brownlee")

# 6. After purchased, construct each one
Empire_State_Building.construct("January 1, 2020")
Tutor_Style_Home.construct("January 5, 2020")
Cape_Cod_Style_Home.construct("January 7, 2020")
Mansion_Style_Home.construct("January 8, 2020")
Flat_Apartment.construct("January 15, 2020")

# 7. Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one. (method written above)

# Empire_State_Building.details()
# Tutor_Style_Home.details()
# Cape_Cod_Style_Home.details()
# Mansion_Home.details()
# Flat_Apartment.details()

# BIRTH OF A CITY:

# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.

# 1. CREATE CITY FOR BUILDINGS
Some_Random_Fictitious_City = City("Some Random Ficticious City", "Mayor McWhatshisface", 2020)

# 2. PUT BUILDINGS IN CITY
Some_Random_Fictitious_City.add_building(Tutor_Style_Home)
Some_Random_Fictitious_City.add_building(Mansion_Style_Home)
Some_Random_Fictitious_City.add_building(Empire_State_Building)
Some_Random_Fictitious_City.add_building(Flat_Apartment)
Some_Random_Fictitious_City.add_building(Cape_Cod_Style_Home)

Some_Random_Fictitious_City.list_buildings()





























