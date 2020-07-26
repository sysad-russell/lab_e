#################################### Task 2 ####################################


################ Task 2.a #################

#TODO: Make a function that:
#       - asks user for their username, password, department.
#       - takes a string (password) and then hashes it.

###########################################

#!/usr/bin/python3

import hashlib # imports Hashing library into current python script


department = input("What department do you belong to?: ")
username = input("What is your username?: ")
password = input("What is your password?: ")

def make_pw_hash(password): # defines the function that creates the hash for the password
    return hashlib.sha256(str.encode(password)).hexdigest # invokes hashing on a provided password



def check_pw_hash(username, password, hash): # defines hash check function against reentry of password
    if make_pw_hash(password) == hash:
        return True

    return False



make_pw_hash(password)



################ Task 2.b #################

#TODO: Create a function that can use a while loop in a real world scenario.

##########################################





################ Task 2.c #################

#TODO: Create a function that can calculate the average numbers in a given list.

##########################################

def averages(*args):
    sum = 0 # creats a set defining a sum of the arguments
    for i in range(len(args)): # defines the set of arguments to be given to sum. Range allows counting over arguments in a set, len provides an int value = the count. i thereby becomes int(each count).
        sum += args[i] #creates a sum of all arguments as defined by args[i]; sum = args[i] + args[i] +..., where i = index of the set of "(args)"
        avg = sum / len(args) # takes average of the sum compared to the number of arguments in "(args)" as an integer value.
    return avg # exits the "for" loop and displays the value stored in the variable, avg.

# example:
# print(averages(10,2,3))
# output = 5.0



################ Task 2.d #################

#TODO: Create a function that can reverse a given number.

##########################################

integer = input("Enter a number: ")
def reverse_num(integer):
    reverse_int = str(integer) [::-1]
    print(reverse_int)

reverse_num(int)
