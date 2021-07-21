#9.3 Make a class User two attributes first,last name an then create several other atrtibutes
#create a method to describe summary of the user's information
#create a method that prints a personalized 
#create a instance and call both methods

class User():
    """Represent a simple user profile."""
    def __init__(self, first_name, last_name, username, email, location):
        """initialize the user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Dsipaly a summary of the user's information"""
        print("Summary of the user's information")
        print("\t",self.first_name.lstrip(), " ", self.last_name)
        print("\tUsername: ", self.username)
        print("\tEmail: ", self.email)
        print("\tLocation: ", self.location)


    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("Welcome back dear ", self.username)   


usernow = User("Jhon", "Erick", "Usernow", "email@gmail.com", "United kingdom")
usernow.describe_user()
usernow.greet_user()
print()
kabroun = User("Oscar", "Raniz", "kabroun", "manco@gmail.com", "Villa juarez")
kabroun.describe_user()
kabroun.greet_user()
