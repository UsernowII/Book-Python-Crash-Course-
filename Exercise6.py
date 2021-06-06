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

import sys


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

#6.5 rivers bucle para imprimir tres mensajes
rivers = {
    'nile': 'egypt',
    'bogota': 'colombia',
    'fraser': 'canada',
    }
for river, city in rivers.items():
    print(f"Este es el rio {river} de {city}")
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("\t",river)
print("\nThe following cities are included in this data set:")
for city in rivers.values():
    print("\t",city)
