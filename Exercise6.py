#6.1 dictionary store information about a person you know. 
"""
person = {
    'first name': "Daniel", 'last name': 
    'Perez', 'age': 28, 'city': "Bogota",
    }

print(person["first name"])
print(person["last name"])
print(person["age"])
print(person["city"])

#6.2 dictionary favorite numbers
favorite_numbers = {
    'daniel': 69, 'jeison': 32,
    'sergio': 17, 'erick': 72,
     }
print(f"daniel's favorite number is {favorite_numbers['daniel']}")
print(f"jeison's favorite number is {favorite_numbers['jeison']}")
print(f"sergiol's favorite number is {favorite_numbers['sergio']}")
print(f"erick's favorite number is {favorite_numbers['erick']}")
"""
#6.3 dictionary ( glosary) words learned and use that like "keys"
"""
glosary = {
    'statement': 'declaracion',
    'list': 'A set de items',
    'tuplas': 'A tuple looks just like a list but with ()',
    }
"""
#6.4 glosary2 recorra el dictionary y haga un print para cada ky-value
"""
glosary = {
    'statement': 'declaracion',
    'list': 'A set de items',
    'tuplas': 'A tuple looks just like a list but with ()',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    }

for word, definition in glosary.items():
    print(f"\n{word.title()}:{definition} ")
"""
#6.5 rivers bucle para imprimir tres mensajes
"""rivers = {
    'nile': 'egypt',
    'bogota': 'colombia',
    'fraser': 'canada',
    }
for river, city in rivers.items():
    print("Este es el rio {} de {}".format(river,city))
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("{:<20}".format(river))
print("\nThe following cities are included in this data set:")
for city in rivers.values():
    print("{:^20}".format(city))"""

#6.6 sondeo cree una lista de las pesonas ue deberian tomar la encuenta y consulte si
# la realizaron o no, enviar una salida
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

candidatos = ["Jen", "Manuel", "Sara", "Miguel"]

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
print("\n")
for candidato in candidatos :
    if candidato.lower() in favorite_languages.keys():
        print(f"Gracias por hacer parte de la encuenta {candidato}")
    else:
        print("{} Cuál es tu lengua favorito ?".format(candidato))"""

#6.7 crear 3 diccionarios agregar a lista y recorrer cada dato e imprimir
"""
animals = ["perro", "gato", "pajaro","elefante","cocodrilo"]
print("Los tres primeros elementos de la lista son")
for animal in animals[:3]:
    print(animal)
print("Los tres  elementos del medio de la lista son")
for animal in animals[1:4]:
    print(animal)
print("Los tres  ultimos elementos de la lista son")
print(animals[-3:])"""
"""
people = []
person= {
    'first name': "Daniel", 'last name': 
    'Perez', 'age': 28, 'city': "Bogota",}
people.append(person)
person= {
    'first name': "Alex", 'last name': 'santos', 
    'age': 33, 'city': "Bogota",}
people.append(person)
person = {
    'first name': "Sesabtian", 'last name': 'Mickey', 
    'age': 23, 'city': "Bogota",}
people.append(person)


for person in people:
    name = (f"{person['first name']} {person['last name']}")
    age = person['age']
    city = person['city']
    print("su nombre es {}".format(name))
    print(f"tiene {age} años")
    print(f"Vive en la ciudad de {city}")
    print()
"""
#6.8
# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
"""
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type' : 'cat',
    'name' : 'gata',
    'owner' : 'Erick',
    }
pets.append(pet)

for pet in pets:
    tipo = pet['animal type']
    name = pet['name']
    owner = pet['owner']
    print("Here's what i know about {}".format(name))
    for x, y in pet.items():
        print("\t" + x + ": " + str(y))
"""
#6.9 Make a dicctionary, three names as keys and store three values , loop throught the dictionary
"""
favorite_places = {
    "jeison" : ["bosa","casa", "trabajo" ],
    "Daniel" : ["Villa del rio", "casa", "homework"],
    "Sergio" : ["bosa", "casa", "tostao"]
    }

for names,places in favorite_places.items():
    print(names.title(), "likes the following places:")
    for place in places:
         print("\t-", place.title())

"""
#6.10 modify program exercise 6.2 for eac person more  than one favorite number
"""
favorite_numbers = {
    'daniel': [69,22,86], 'jeison': [32,25,86],
    'sergio': [17,86,58], 'erick': [72,86,45]
     }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}´s favorite numbers are: ")
    for number in numbers:
        print("-", number)

"""
#6.11 Make a dictionary called countrys. use three cities as keys and store information about these countrys
#in another one dictionary

countrys = {
    "Colombia" : {"capital city": "Bogota", "poblation" :50347000 , "Nationality" : "Colombian"},
    "Mexico" : {"capital city": "MDX", "poblation": 1000356891, "Nationality": "Mexican"},
    }

for country, country_info in countrys.items():
    capital_city = country_info["capital city"]
    poblation = country_info["poblation"]
    nationality = country_info["Nationality"].title()

    print(country,"\n\tYour capital is", capital_city)
    print("\tPoblation are :",poblation, "population.")
    print("\tThe nationality is", nationality)






