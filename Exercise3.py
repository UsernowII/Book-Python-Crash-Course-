#3.1 litas
"""
name = ["daniel", "sergio", "jeison"]
print(name[0].title())
print(name[1])
print(name[2])

#3.2 greeting printing each person's name one at a time

greeting = "Hi " + name[0].upper() + " pinche putito!"
print(greeting)
print("Hi " + name[1].upper() + " pinche putito!")

greeting = "Hi " + name[2].upper() + " pinche putito!"
print(greeting)
"""

#3.3 my own list ( mode of trasportation)
"""
champs_lol = ["rengar" , "leblanc" , "fizz" , "kaisa" , " lucian" ]
oscar = "Kabroun es un puto manco con" + champs_lol[4]
print(oscar)"""

#3.4 lists for dinner
"""
dinner = ["Fredy Mercury" , "Reina Isabel" , "Bender"]
invitation = "Hi " + dinner[0] + " Do you wanna go to dinner tonight ?"
print(invitation)

invitation = "Hi " + dinner[1] + " Do you wanna go to dinner tonight ?"
print(invitation)

invitation = "Hi " + dinner[2] + " Do you wanna go to dinner tonight ?"
print(invitation)

guest = dinner[0].title()
print("Hi " + guest+ " Do you wanna go to dinner tonight?")
"""
#3.5 list change guest
"""
dinner = ["Fredy Mercury" , "Reina Isabel" , "Bender"]
guest = dinner[1]
print(guest + " no puede asistir a cenar esta noche.")
dinner[1] = "El papa"
print(dinner)

guest = dinner[0]
print("Hi " + guest + "\nDo you wanna go to dinner tonight?")
guest = dinner[1]
print("Hi " + guest + "\nDo you wanna go to dinner tonight?")
guest = dinner[2]
print("Hi " + guest + "\nDo you wanna go to dinner tonight?")

#3.6 more guests

print("I got a bigger table")
dinner.insert(0, "Rafa nadal")
dinner.insert(3, "Elon musk")
dinner.append("Willie wonka")

guest = dinner[0].title()
print("Hi " + guest + " Do you wanna go to dinner tonight?")
guest = dinner[1].title()
print("Hi " + guest + " Do you wanna go to dinner tonight?")
guest = dinner[2].title()
print("Hi " + guest + " Do you wanna go to dinner tonight?")
guest = dinner[3].title()
print("Hi " + guest + " Do you wanna go to dinner tonight?")
guest = dinner[4].title()
print("Hi " + guest + " Do you wanna go to dinner tonight?")
guest = dinner[5].title()
print("Hi " + guest + " Do you wanna go to dinner tonight?")


#3.7

print(dinner)
print("excuse me , just i can invite to two guest for dinner")
guest = dinner.pop()
print("sorry," + guest + " table is full")
guest = dinner.pop(0)
print("sorry," + guest + " table is full")
guest = dinner.pop(1)
print("sorry," + guest + " table is full")
guest = dinner.pop(1)
print("sorry," + guest + " table is full")

#invitar a cenar a los restantes de la lista

guest = dinner[0]
print("Hi " + guest.title() +" Do you can still  go to dinner tonight ?")
guest = dinner[1]
print("Hi " + guest.title() +" Do you can still  go to dinner tonight ?")
del dinner[0]
del dinner[0]
print(dinner)
"""

#3.8 Organizing a List

cities = ['CDMX', 'Santa Marta', 'Madrid', 'Ontario', 'Soacha']
print("original")
print(cities)
print("\nordenada alfabeticamente")
print(sorted(cities))
print("original")
print(cities)
print("\nordenada alfabetico inverso")
print(sorted(cities, reverse=True))#alfabeticamente reversa
print("original")
print(cities)
print("\nreverse")
cities.reverse()
print(cities)
print("\n reverse al reverse")
cities.reverse()
print(cities)
print("\nalfabetica permanente")
cities.sort()
print(cities)
print("\nreverse alfhabetical permanently")
cities.sort(reverse=True)
print(cities)

#3.9
dinner = ["Fredy Mercury" , "Reina Isabel" , "Bender"]
print((len(dinner)))