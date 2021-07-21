#8.1 Write a function
"""
def display_message():
    print("I learned how to make a function with any parameters")
    print("I learned how to make a function without parameters")

display_message()
"""
#8.2 write a function that acceptos one parameter
"""
def favorite_book(book):
    print(f"{book} is one of my favorite books")


favorite_book("Python Crash Course")
"""
#8.3 make a function call it and call it again with keywords arguments
"""
def make_shirt (size, message):
    print("Im going to make a", size, "t-shirt")
    print('it will say, "', message, '"')

make_shirt("large", "I love python")
make_shirt(size = "medium", message="I love python")
"""

#8.4 modify a function 8.3 with arguments as default
"""
def make_shirt (size= "large", message= "I love Python"):
    print("Im going to make a", size, "t-shirt")
    print('it will say, "', message, '"')

make_shirt()
make_shirt(size = "medium")
make_shirt("medium", "Programmers are loppy")"""

#8.5 write a function that accepts 2 arguments, parameter city as defautl
"""
def describe_city(city, country = "Colombia"):
    print(f"{city} is in {country}")


describe_city("Bogota")
describe_city("MDX", "Mexico")
describe_city("valledupar")
"""
#8.6 Write a function that takes in the name of a city and its country and return full string
"""
def city_country(city,country):
    return(city.title()+ " "+ country.title())


city = city_country("santigado", "Chile")
print(city)
city = city_country("Buenos aires", "Argentina")
print(city)
"""
#8.7 Wirte a functiono and buiild a dictionary that contains artis-album and return it
"""
def make_album(artist, album, tracks = ""):
    albums = {
        "artist" : artist.title(),
        "album" : album.title(),
    }
    if tracks:
        albums["tracks"] = tracks.title()
    return albums

album = make_album("Metalica", "black album")
print(album)
album = make_album("Incubus", "Greatest hits")
print(album)
album = make_album("Metalica", "black album", "15")
print(album)
"""

#8.8 With Exercise 8.7 add a while loop for to permit do input for teh user
"""
def make_album(artist, album, tracks = ""):
    albums = {
        "artist" : artist.title(),
        "album" : album.title(),
    }
    if tracks:
        albums["tracks"] = tracks.title()
    return albums


while True:
    print("Enter '<q>' at any time to stop")
    title =input("\nWhat album are you thinking of ?")
    if title == 'quit':
        break
    
    artist =  input("who's the artist ?")
    if artist == 'quit':
        break
    
    album = make_album(artist, title)
    print(album)
    

print("\nThanks for responding!")
"""

#8.9 Make a list, pas the list to a function, print each name in the list
"""
magicians_names = ["daniel", "sergio", "jeison"]

def show_magicians():
    for name in magicians_names:
        print("The name of magician is ",name.title())

show_magicians()
"""
#8.10 copu from list 8.9 , make a function that modifies the list adding teh phrase"the great"
"""
magicians_names = ["daniel", "sergio", "jeison"]

def show_magicians(magicians_names):
    #Print the name of each magician in the list
    for name in magicians_names:
        print(name.title())


def make_great(magicians_names):
    #Add " the Great!" to each magician's name.
    #build a new list to hold the great magicians
    great_magicians = []

    #Make each magician great, and add it to great_magicians.
    while magicians_names:
        magician = magicians_names.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    #Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians_names.append(great_magician)


show_magicians(magicians_names)
print("\n")
make_great(magicians_names)
show_magicians(magicians_names)
"""

#8.1 with exercise 8.10, call the function make_great with a copy of the list of magicians_names
#return the new list and store in a separate list
"""
magicians_names = ["daniel", "sergio", "jeison"]

def show_magicians(magicians_names):
    #Print the name of each magician in the list
    for name in magicians_names:
        print(name.title())


def make_great(magicians_names):
    #Add " the Great!" to each magician's name.
    #build a new list to hold the great magicians
    great_magicians = []

    #Make each magician great, and add it to great_magicians.
    while magicians_names:
        magician = magicians_names.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    #Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians_names.append(great_magician)

    return magicians_names


show_magicians(magicians_names)
print("\nlist Great magicians :")
great_magicians = make_great(magicians_names[:])
show_magicians(great_magicians)
print("\nOriginal list magicians")
show_magicians(magicians_names)
"""

#8.12 Write a function that accepts several parameters, it should have one paremeter that collects n arguments
"""
def make_sandwich (*items):
    #Make a sandwich with the given items
    print("\nI'll make you a great sandiwch: ")       
    for item in items:
        print(f" ... adding {item} to your sandwich" )
    print("your sandwich is ready")

make_sandwich("roast beef", "cheddar chesse", "lettuce")
make_sandwich("roast beef", "peanut butter","honey mustard", "lettuce")
"""
#8.13 start with a copy user_profile.py page 153. build the function with your information
"""
def build_profile(first, last, **user_info):
    #Build a dictionary containing everything we know about a user.
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Jhon', 'Erick',
                             location=' United Kingdom',
                             height='1.69 cm', weight = "71.6 kg")
print(user_profile)
"""

#8.14 Write a function store information about the car < manufacturer> <model>
# and accept an arbitrary number of keyword arguments.store in dictionary
"""
def make_car(manufacturer, model, **feautres):
    car= {
        "manufacturer": manufacturer,
        "model " : model
    }

    for feature,value in feautres.items():
        car[feature] = value

    return car
car = make_car("subaru", "outback", color = "blue", tow_package = True)
print(car)
"""
#8.15 import functions from modules
#module name is " modulo "
#import modulo  #importa todo el modulo
#from modulo import function_name  # importa x funcion del modulo
#from modulo import function_name as fn #importa x funcion del modulo con un alias
#import modulo as md # importa el modulo con un alias
#from modulo import* # importa el modulo sin necesidad de usar alias en las funciones