# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city.
import datetime

# 1. Create a class named Building.
class Building:

    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
    
# 2. Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.
    def construct(self, date_constructed):
        self.date_constructed = datetime.datetime.now()

# 3. Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.
    def purchase(self, owner):
        self.owner = owner

    def details(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed.strftime('%m-%d-%y')} and has {self.stories} stories.")

# 4. Create 5 building instances
Empire_State_Building = Building("New York", 102)
Tutor_Style_Home = Building("Seattle", 2)
Cape_Cod_Style_Home = Building("Denver", 2)
Mansion_Home = Building("Bainbridge Island", 3)
Flat_Apartment = Building("Nashville", 1)

# 5. Have each one get purchased by a real estate magnate
Empire_State_Building.purchase("Caroline Brownlee")
Tutor_Style_Home.purchase("Caroline Brownlee")
Cape_Cod_Style_Home.purchase("Caroline Brownlee")
Mansion_Home.purchase("Caroline Brownlee")
Flat_Apartment.purchase("Caroline Brownlee")

# 6. After purchased, construct each one
Empire_State_Building.construct("January 1, 2020")
Tutor_Style_Home.construct("January 5, 2020")
Cape_Cod_Style_Home.construct("January 7, 2020")
Mansion_Home.construct("January 8, 2020")
Flat_Apartment.construct("January 15, 2020")

# 7. Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one. (method written above)
Empire_State_Building.details()
Tutor_Style_Home.details()
Cape_Cod_Style_Home.details()
Mansion_Home.details()
Flat_Apartment.details()