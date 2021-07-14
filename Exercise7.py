# Inputs

#7.1 Rental Car input
"""
rental_car = input("what kind of car would you like rental ?")
print("Let me see if i cand find you a ", rental_car)
"""

#7.2 input Restaurant seating with if statament
"""
table_size = int(input("How many people are in their dinner group?"))

if table_size > 8 :
    print("Sorry. You'll have to wait for a table")
else:
    print("Your table is ready, come on")
"""

#7.3 ask the use for a nmber an the report this number is multile of 10 or not.
"""
number = int(input("Give me one number"))

if number % 10 == 0 :
    print(f"this {number} is a multiple of 10")
else:
    print(f"this {number} isn't a multiple of 10")
"""
# loop WHILE

#7.4 loop while with break
"""
prompt = ("Please what topping would you like on your pizza ?:")
prompt +=("Enter 'quit' when you are finished. ")

while True:
    message = input(prompt)
    if message == 'quit':
        break
    print("I’ll add " +message+ " to their pizza")
"""

#7.5 A movie theater prices depending on a person's age
#if under of 3 is free / 3 to 12 ticek $10 / >12 $15


prompt = "How old are you ?\nEnter 'quit' when you are finished. "
"""
while True:
    age = input(prompt)
    if age == 'quit':
        print("Thank you for your visit")
        break
    age = int(age)
    if age < 3: 
        print("You get in free !!")
    elif age >=3 and age <13:
        print("Your ticket is $10")
    else:
        print(("Your ticket is $15")) 
"""

#7.6 Exercise 7.4 several ways
# with conditional 
"""
prompt = ("Please what topping would you like on your pizza ?:")
prompt +=("\nEnter 'quit' when you are finished. ")
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("I’ll add " +message+ " to their pizza")
"""
#with flag
"""
prompt = ("Please what topping would you like on your pizza ?:")
prompt +=("\nEnter 'quit' when you are finished. ")
flag = True

while flag:
    message = input(prompt)
    if message == 'quit':
        flag =  False
        print("Thank you for your visit")
    else:
        print("I’ll add " +message+ " to their pizza")
"""    
#7.7 infinite Loop
"""
x = 10 
while x :
    print(x)
"""   

#7.8 make a list of sandwichs and other empty list, prepare each sandwich and move to list finished sandwichs
"""
sandwich_orders = ["atun", "pollo", "subway"]
finished_sandwiches = []

while sandwich_orders:
    make_sandwich = sandwich_orders.pop()
    print("I'm working in your ", make_sandwich + " sandwich")
    finished_sandwiches.append(make_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a "+ sandwich+ " sandwich" )
"""

#7.9 Using list 7.8 , make sandwich "pastrami" x3 times
#remove "pastrami" from list and print sold out this topping
"""
sandwich_orders = ["pastrami", "atun", "pollo","pastrami", "subway","pastrami"]
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today")

while sandwich_orders:
    for sandwich in sandwich_orders:
        if "pastrami" == sandwich:
            sandwich_orders.remove(sandwich)
    make_sandwich = sandwich_orders.pop()
    print("I'm working in your ", make_sandwich + " sandwich")
    finished_sandwiches.append(make_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a "+ sandwich+ " sandwich" )
"""
#7.9 write program throught  loop while that polls user about their dream vacation
responses = {}
prompt_name = "what's your name? "
prompt_place = "If you could visit one place in the world, where would it be ? "

response = ""
while response.lower()!= "no" :
    name = input(prompt_name)
    place = input(prompt_place)
    response = input("\nWould you like to let someone else respond ? (yes/no) ")
    responses[name] = place

print("----Results----")
for name,place in responses.items():
    print(name, "Would like to visit ", place)