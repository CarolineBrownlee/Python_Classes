# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city.
import datetime

# 1. Create a class named Building.
class Building:

    def __init__(self, name, address, stories):
        self.name = name
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
         return (f"{self.name} is located at {self.address} and was purchased by {self.owner} on {self.date_constructed.strftime('%m-%d-%y')}. It has {self.stories} stories.")
        
        # print(f"* {self.name} is located at {self.address} and was purchased by {self.owner} on {self.date_constructed.strftime('%m-%d-%y')}. It has {self.stories} stories.")

# LESSON CONTINUED in URBAN PLANNER TWO EXERCISE. Reference urbanPlannerTwo.py for logic.