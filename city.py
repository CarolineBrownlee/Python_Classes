# In the previous Urban Planner exercise, you practiced defining custom types to represent buildings. Now you need to create a type to represent your city. Here are the requirements for the class. You define the properties and methods.

# Name of the city.
# The mayor of the city.
# Year the city was established.
# A collection of all of the buildings in the city.
# A method to add a building to the city.
# Remember, each class should be in its own file. Define the City class in the city.py file.
from urbanPlanner import Building

class City:

    def __init__(self, city_name, city_mayor, city_year_established):
        self.city_name = city_name
        self.city_mayor = city_mayor
        self.city_year_established = city_year_established
        self.city_buildings = list()

    def add_building(self, new_building):
        self.city_buildings.append(new_building)

    # def building_counter(self):

    def list_buildings(self):
        print(f"{self.city_name} has the following buildings: ")
        i = 1
        for building in self.city_buildings:
            print(f"{i}. " + building.details()) 
            i = i + 1
        


            
