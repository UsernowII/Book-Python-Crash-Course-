#9.1 create a class  method constructor with 2 attributes and 2 method
#make a instance called restaurant from your class
#print 2 attributes individually an then call both methods.
class Restaurant():
    """A class representing a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " server wonderfull" + self.cuisine_type
        print(msg)
        print("\n")
        

    def open_restaurant(self):
        """Display a message that t he restaurant is open."""
        msg = self.name + " is open, Come on in!"
        print(msg)
        print("\n")

restaurant = Restaurant("jhon's kitchen", "Pizza")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.1 create three instances from the class and call describe_restaurante for each instance

delicious_thin = Restaurant("Las delicias del flaco", "Fast food")
delicious_thin.describe_restaurant()

parrilla_gourmet = Restaurant("Pariilla gourmet", "high cook")
parrilla_gourmet.describe_restaurant()

the_edge = Restaurant("La orillla", "casero")
the_edge.describe_restaurant()