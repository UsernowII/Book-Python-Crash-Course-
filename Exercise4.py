#4.1 use a for loop to print name of each from list
"""
pizzas = ["pollo con champiñon" , "Hawaiana" , "peperoni" ]
for piza in pizzas:
    print(piza)
print("\n")
for piza in pizzas:
    print("Mi piza favorita es la de " + piza)
print("\nI really love pizza")"""


#4.2 list animals
"""
animals = ["perro", "gato", "pajaro"]
for animal in animals :
    print("Un " + animal + " seria una gran mascota.")
print("Pero, cualquiera de estos podria ser una buena mascota")"""

#4.3 imprime los numeros del 1 -20
"""
for number in range(1,21):
    print(number, end= " ")
print()"""
#4.4 make to list 1-1.000.000 e imprimir con for 
"""
numbers = list(range(1,1000001))
for num in numbers:
    print(num)"""
#4-5 sumar lista , sacar minimo y maximo
"""
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))"""

#4.6 lista odd numbers 1-20
"""
for number in range(1,21,2):
    print(number)"""

#4.7 make a list multiples of 3 from 3 to 30, print
"""
three = list(range(3,31,3))
for number in three:
    print(number)
print(three) # lista creada"""

#4.8 cubes primeros 10 numeros and use for bucle print each cube
"""
cubes = []
for number in range(1,11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)"""

#4.9 list comprehension for 10 first cubes
"""
cubes = [number**3 for number in range(1,11)]
print(cubes)
for cube in cubes:
    print(cube)"""

#4.10 use a list and use slice for print first 3 items

"""animals = ["perro", "gato", "pajaro","elefante","cocodrilo"]
print("Los tres primeros elementos de la lista son")
for animal in animals[:3]:
    print(animal)
print("Los tres  elementos del medio de la lista son")
for animal in animals[1:4]:
    print(animal)
print("Los tres  ultimos elementos de la lista son")
print(animals[-3:])"""

#4.11 copiar una lista y agregar elementos para cada una
"""
pizzas = ["pollo con champiñon" , "Hawaiana" , "peperoni" ]
friend_pizzas = pizzas[:]
pizzas.append("mexicana")
friend_pizzas.append("vegetariana")
print("mis favoritas pizzas son : ")
for pizza in pizzas[:]:
    print(pizza)
print("Las pizzas favoritas de mi amigo son: ")
for pizza in friend_pizzas[:]:
    print(pizza)
"""
#4.12
"""
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 

my_foods.append('cannoli') 
friend_foods.append('ice cream') 

print("My favorite foods are:")
for food in my_foods[:]:
    print(food)
print("\nMy friend's favorite foods are:")
for pizza in friend_foods:
    print(pizza)
"""
#4.13 tuplas 

foodbuffet = ("Paella", "lechona", "pechuga", "lomo", "sopa de camarones")
print("Nuestro menu")
for food in foodbuffet:
    print(food)
#foodbuffet[2] = "frijolada"
foodbuffet = ("Paella", "caviar", "pechuga", "lomo", "crema de mazorca")
print("nuestro menu fue actualizado")
print("Nuestro menu")
for food in foodbuffet:
    print(food)
