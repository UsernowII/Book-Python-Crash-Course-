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
"""
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
    print("pera")"""

#5.8 list username for admin message especial, for other users greetin generic
"""
username = ["admin", "erick", "patricia", "claudia", "manuel"]
for user in username :
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello" , user ,"welcome back!!")"""

#5.9add if statement make sure the list of users is not empty.
"""
#username = ["admin", "erick", "patricia", "claudia", "manuel"]
username = [] # emptylist
if username :
    for user in username :
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello" , user ,"welcome back!!")
else :
    print("We need to find some users")"""

#5.10 create a program that simulates
#how websites ensure that everyone has a unique username. 
#recorra la lista y compruebe si ya existe el nick, case sensitive
"""
current_users = ["Admin", "erick", "patricia", "claudia", "manuel"]
new_users = ["admin", "maira", "sara", "fernando", "ERICK"]
current_users_lower = [userlow.lower() for userlow in current_users]
#current_users_lower = []  crear lista de usuarios actuales en miniscula
#for user in current_users:
#    current_users_lower.append(user.lower())
for new_user in new_users :
    if new_user.lower() in current_users_lower :
            print("Este usuario ya existe, ingrese un nuvo nombre de usuario")
    else:
        print("El nombre de usuario esta disponible")
print(new_users) # la lista original sigue con letras mayusculas
"""

#5.11 numeros ordinales, use if-elif-else

ordinal_numbers = list(range(1,10))
for number in ordinal_numbers:
    if number == 1 :
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+"nd")
    elif number ==3 :
        print(str(number)+"rd")
    else:
        print(str(number)+"th")

