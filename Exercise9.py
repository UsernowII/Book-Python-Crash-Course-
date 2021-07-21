class Dog():
    """A simple attempt to model a dog"""
    def __init__(self, name, age):              #3       
        """Initialize name and age attributes."""
        self.name = name #4
        self.age = age

    def sit (self): #5
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + "rolled over!")        
#instance object "My_dog"
my_dog = Dog("Whili", 6)
#instamce object your_dog
your_dog= Dog("lucy", 3)
#Object 1
print("My dog's name is ", my_dog.name.title())
print("My god is "+ str(my_dog.age)+ " years old")
#Object 2
print("My dog's name is ", your_dog.name.title())
print("My god is "+ str(your_dog.age)+ " years old")


my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()
