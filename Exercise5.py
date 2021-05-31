#5.1 if tests
"""
car = "Renault"
print("car is == 'Renault', I predict True")
print(car == "Renault")
car2 = "Renault"
print("car is == 'BMW', I predict False")
print(car == "BMW")
"""
#5.2 
"""
car = ["renault", "BMW", "Mazda", 1 , 5 , 10]
print(car[1].upper() == "BMW")
print(car[2].title() == "Mazda")
print(car[0] == "Renault")

print("renault" in car)
print("mercedez" in car)

car2 = "mercedez"
if car2 not in car :
    print("este carro no esta en la lista" )"""

#5.3 alien color video game
"""
alien_color = "green"
if alien_color == "amarillo" :
    print("Alien esta muerto, jugador gana 5 puntos")
elif alien_color == "green" :
    print("Alien esta muerto, jugador gana 5 puntos")"""

#5.4 choose color for alien, green 5 puntos , not green 10 puntos
"""
alien_color = "green"
if alien_color == "green" :
    print("Jugador gana 5 puntos por disparar al alien")
else :
    print("Jugador gana 10 puntos por disparar al alien")


if alien_color == "yellow" :
    print("Jugador gana 5 puntos por disparar al alien")
else:
    print("Jugador gana 10 puntos por disparar al alien")"""

#5.5 Choose a color for an alien as you did in Exercise 5-3, and
#write an if-else chain.
"""
alien_color = "red"
if alien_color == "green" :
    print("Jugador gana 5 puntos por disparar al alien")
if alien_color == "yellow" :
    print("Jugador gana 10 puntos por disparar al alien")
else:
    print("Jugador gana 15 puntos por disparar al alien")"""

#5.6 write change if-else-elif for stage of life 
"""
age = 28
if age < 2:
    print("Is a baby")
elif age <4:
    print("is a toddler")
elif age <13:
    print("is a kid")
elif age <20:
    print("is a teenager")
elif age <65:
    print("is an adult")
else:
    print("is an elder")"""

#5.7 list fruits 5 ifs statements match diferentes fruits in the list
favorite_fruit = ["naranja", "banano", "manzana", "mango",]
if "naranja" in favorite_fruit:
    print("naranja")
if "zapote" in favorite_fruit:
    print("zapote")
if "banano" in favorite_fruit:
    print("banano")
if "mango" in favorite_fruit:
    print("mango")
if "pera" not in favorite_fruit:
    print("pera")


