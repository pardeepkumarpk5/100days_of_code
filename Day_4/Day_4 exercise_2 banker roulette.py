# random paying the bill
import random

# asking the user for name list
names_in_string = input(
    'type the names of your friends who want to share your burden ')

# converting string into a list using split function
names_list = names_in_string.split(',')

# creating a random number for our name list
random_number = random.randint(0, (len(names_list) - 1))


# printing out random name
random_name = names_list[random_number]
print('person who is going to pay the bill today is ', random_name)
