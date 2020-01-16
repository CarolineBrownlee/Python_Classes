class Pizza:
# 1. Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.
    def __init__(self, size, crust):
        self.size = size
        self.crust = crust
        self.toppings = list()
    
# 2. Add a method for interacting with a pizza's toppings, called add_topping.
    def add_topping(self, new_topping):
        self.toppings.append(new_topping)

# 3. Add a method for outputting a description of the pizza (sample output below).
    def order(self): 
        toppings = " and ".join(self.toppings)
        print(f"I would like a {self.size} inch, {self.crust} crust pizza with {toppings}.")

# 4. Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

veggie_lovers = Pizza(12, "deep dish")
veggie_lovers.add_topping("mushroom")
veggie_lovers.add_topping("tomatoes")
veggie_lovers.add_topping("pineapple")
veggie_lovers.order()

personal_pizza = Pizza(10, "regular")
personal_pizza.add_topping("pineapple")
personal_pizza.add_topping("ham")
personal_pizza.order()
