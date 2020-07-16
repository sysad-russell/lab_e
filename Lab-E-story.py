#!/usr/bin/python3

import random


bar = "*"
print("")
print(bar * 68)
print("This is a simple Python3 story.")
print(bar * 68)
print("- sysadRussell")
print("")

pest = [ "starving coyote", "keen-eyed hawk", "sly rat", "pan-handling pigeon" ]
borough = [ "Queens", "The Bronx", "Manhattan", "Brooklyn", "Staten Island"]
action1 = [ "scurried toward", "swooped toward" ]
action2 = [ "ravenously devoured", "tore haphazardly through"]
food = [
"a sack of sweet-potato peels", "slimey bag of chicken strips",
"moldy beef stew", "slew of rotten eggplants","sour bag of carrot sticks",
"partly devoured melon", "discarded pizza-pie", "mound of trash"
]

pest_act = {
pest[0]:action1[0],
pest[1]:action1[1],
pest[2]:action1[0],
pest[3]:action1[1]
}



###################### MENU #########################



############## ANIMAL ##############
Animal_choice = '0'

if Animal_choice == '0':
    print(f"Animal Choice: Choose 1 of 4 choices")
    print(f"Choose 1 for {pest[0]}")
    print(f"Choose 2 for {pest[1]}")
    print(f"Choose 3 for {pest[2]}")
    print(f"Choose 4 for {pest[3]}")

Animal_choice = input('Present your selection: ')

if Animal_choice == '1':
	Animal_choice = pest[0]
elif Animal_choice == '2':
	Animal_choice = pest[1]
elif Animal_choice == '3':
	Animal_choice = pest[2]
elif Animal_choice == '4':
	Animal_choice = pest[3]
else: print(f"invaild input""\n")

############# ACTION #################

action_choice = '0'

if action_choice == '0':
    print(f"\n""Animal Action: Choose 1 of 2 choices")
    print(f"Choose 1 for {action2[0]}")
    print(f"Choose 2 for {action2[1]}")

Action_choice = input(f'Present your selection: ')

if Action_choice == '1':
	Action_choice = action2[0]
elif Action_choice == '2':
	Action_choice = action2[1]
else:	print("invaild input")


############# FOODS #################


Food_choice = '0'

if Food_choice == '0':
	print(f"\n""Food Choice: Choose 1 of 8 choices")
print(f"Choose 1 for {food[0]}")
print(f"Choose 2 for {food[1]}")
print(f"Choose 3 for {food[2]}")
print(f"Choose 4 for {food[3]}")
print(f"Choose 5 for {food[4]}")
print(f"Choose 6 for {food[5]}")
print(f"Choose 7 for {food[6]}")
print(f"Choose 8 for {food[7]}")


Food_choice = input('Present your selection: ')

if Food_choice == '1':
	Food_choice = food[0]
elif Food_choice == '2':
	Food_choice = food[1]
elif Food_choice == '3':
	Food_choice = food[2]
elif Food_choice == '4':
	Food_choice = food[3]
elif Food_choice == '5':
	Food_choice = food[4]
elif Food_choice == '6':
	Food_choice = food[5]
elif Food_choice == '7':
	Food_choice = food[6]
elif Food_choice == '8':
	Food_choice = food[7]

else: print(f"invaild input""\n")


######### BOROUGHS ################


Borough_choice = '0'

if Borough_choice == '0':
	print(f"\n""Borough Choice: Choose 1 of 5 choices")
print(f"Choose 1 for {borough[0]}")
print(f"Choose 2 for {borough[1]}")
print(f"Choose 3 for {borough[2]}")
print(f"Choose 4 for {borough[3]}")
print(f"Choose 5 for {borough[4]}")



Borough_choice = input('Present your selection: ')

if Borough_choice == '1':
	Borough_choice = borough[0]
elif Borough_choice == '2':
	Borough_choice = borough[1]
elif Borough_choice == '3':
	Borough_choice = borough[2]
elif Borough_choice == '4':
	Borough_choice = borough[3]
elif Borough_choice == '5':
	Borough_choice = borough[4]

else: print(f"invaild input""\n")

# testing code
print(f"""
	In {Borough_choice}, a borough of New York, a {Animal_choice} quickly
{pest_act[Animal_choice]}, and {Action_choice}, a {Food_choice}.
""")
#
#print(pest[{food[7]}0:])
#
#
#
#
#
