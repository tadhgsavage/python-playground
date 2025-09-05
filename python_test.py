#Printing basic message
print("Hello World!")

#Printing with varibale
message = ("Hello Tadhg")
print(message)

#redefining variable
message = ("Hello, reader")
print(message)

# Some basic name and methods attached
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Using an f string to tie a name together
first_name = 'ada'
last_name = 'lovelace'
full_name = (f"{first_name} {last_name}")
print(full_name.title())

# Using an f string to make a sentence from a created variable
message = (f"Hello, {full_name.title()}!")
print(message)

print("\t" + message)
print (f'\t{message}')
print ("\t",message)

# Stripping white spaces with the strip method
message = (" python ")
print (message.lstrip())
print (message.rstrip())
print (message.strip())

# Removing prefixes with the removepreffix method and suffixes 
website = ("https://apple.com")
print(website.removeprefix("https://"))

# Remove suffix
website = ("https://apple.com")
print(website.removesuffix(".com"))

# Remove both prefix and suffix 
webiste = ("https://apple.com")
print(website.removeprefix("https://").removesuffix(".com"))

# Multiple assignment with numbers
x, y, z = 1, 2, 3
print(x,y,z)

# Constants 
MAX_CONECTIONS = 5_000

# Lists 
cars = ['bugatti', 'ford', 'ferrari']
print(cars)
print(cars[0])
print(cars[0].title())

# Accessing elements on the last of a list
print(cars[-1].title())

# Now putting into an f string
cars = ['bugatti', 'ford', 'ferrari']
message = (f'My favourite car is a {cars[-1].title()}')
print(message)

# Modifying elements in a list
cars = ['bugatti', 'ford', 'ferrari']
cars[0] = 'bentley'
print(cars)

# Adding an element to a list
cars.append('citroen')
print(cars)

# One can start with an empty list and just append all items in
cars = []
cars.append("ford")
cars.append("bugatti")
cars.append("fiat")
print(cars)

# One can also insert an elemet into a list
cars.insert(1, "bmw")
print(cars)

# Removing an element from a list using the del statement
del cars[0]
print(cars)

# Removing items using the pop method
popped_car = cars.pop()
print(cars)
print(popped_car)

# Making this useful
cars = ["fiat", 'ford', 'bentley', 'ferrari']
last_car = cars.pop(1)
message = (f"The last car I owned was a, {last_car.title()}.")
print(message)

# If position is not known one can use the remove method to remove it instead 
cars = ["fiat", 'ford', 'bentley', 'ferrari']
too_expensive = "fiat"
cars.remove(too_expensive)
message = (f"{too_expensive.title()}, was too expensive for me!")
print(message)

# Sorting a list permanently with the sort method 
cars = ["fiat", 'ford', 'bentley', 'ferrari']
cars.sort()
print(cars)

# Reversing the order with reverse=True
cars = ["fiat", 'ford', 'bentley', 'ferrari']
cars.sort(reverse=True)
print(cars)

# One can sort a list temporarily with the sorted function
cars = ["fiat", 'ford', 'bentley', 'ferrari']
print("here is the original order of the list")
print(cars)
print("\nHere is the sorted list")
print(sorted(cars))
print("\nHere is the original list again")
print(cars)

# Printing a list in reverse order
cars.reverse()
print(cars)

# One can reverse back again by applying the reverse method again
cars.reverse()
print(cars)

# Finding the length of a list
print(len(cars))

# Looping through a list 
magicians = ['alice', 'chiara', 'toby']
for magician in magicians:
    print(magician.title())

# Building the loop out to have a sentence
magicians = ['alice', 'chiara', 'toby']
for magician in magicians:
    print(f'Hey, {magician.title()}, that was a great trick!')

# One can also put as much as they want in a loop and the loop will loop it provided its inside of the loop
magicians = ['alice', 'chiara', 'toby']
for magician in magicians:
    print(f"\nHey, {magician.title()}, that was a great trick!")
    print(f"Well done {magician.title()}!")

# Using the range fucntion to generate a list of numbers 
for value in range(1, 6):
    print(value)

# Using range to make a list of numbers
numbers = list(range(6))
print(numbers)

# We can add a thrid argument into the range funciton which is like a delimiter
# List of even numbers
even_numbers = list(range(0, 11, 2))
print(even_numbers)

# Creating a list of squared numbers 
# Start with an empty list 
sqaures = []
for value in range(1, 11):
    square = value ** 2
    sqaures.append(square)
print(sqaures)


# Performing simple statistics with python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

# Using a list comprehension to create a list of squares 
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Slicing lists 
players = ['ellie', 'sarah', 'nole', 'chiara', 'toby']
print(players[0:3])
print(players[1:4])
# Omiting the first number will mean python starts at the begining of a list
print(players[:4])
# Ommiting the last likewise will make python continue to the end as well
print(players[1:])
# Negative numbers also work
# This below prints the last three names in a list and if the list continued to grow it would continue printing the last 3 names
print(players[-3:])


# We can use a slice to also loop through part of a list
players = ['ellie', 'sarah', 'nole', 'chiara', 'toby']
for player in players[:3]:
    print(player.title())

# To copy a list take a slice of the entire list 
my_foods = ['pizza', 'pasta', 'bread', 'sauce']
friends_food = my_foods[:]
my_foods.append("garlic")
friends_food.append("sugar")
print(my_foods)
print(friends_food)

# Python refers to values that cannot change as immutable 
# Tupples are simply immutable lists 
# Tupples look just like a list but instead of using square brackets we use paranthesis 
# Tupple of dimensions 
dimensions = (200, 80)
print(dimensions[0])
print(dimensions[1])

# Tupples are technicaly defined by the comma and nor parenthesis, that is used so it is neater
# If you wanted to create a tupple with just one element you would need to insert a trailing comma
location = (30, )

# Although you may not modify a tupple you can redefine it

# If Statements 
cars = ['bugatti', 'honda', 'bmw', 'mercedes']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# A double == sign signifies a search for equality and a != sign searches for inequality a single = sign sets it = to
car = 'bmw'
if car == 'bmw':
    print('True')
else:
    print('False')
if car != 'audi':
    print('Not and Audi')
else:
    print('Car is an Audi')


# Pizza restaurant example
requested_topping = 'mushrooms'
if requested_topping != 'mushrooms':
    print('Dont use mushrooms!')
else:
    print("Add mushrooms")

# One can also do numerical comparisons 
# Set age at 20
age = 20
if age >= 18:
    print('They can enter')
else:
    print('They may not enter')

# Or one can look for an exact number say in a guessing game
guess = 20
if guess != 42:
    print('Wrong Try Again!')
else:
    print('Correct!')


# Incorporating AND and OR into statements
age_0 = 18
age_1 = 20

if (age_0 >= 18) and (age_1 >= 18):
    print('PASS')
else:
    print('FAIL')

if (age_0 >= 18) or (age_1 >= 18):
    print('PASS')
else:
    print('FAIL')

# Using "in" to check the presense of an item in a list
cars = ['bugatti', 'honda', 'bmw', 'mercedes']
car = 'bugatti'
if car in cars:
    print(f'{car}, is already present.')
else:
    print(f'{car}, is not present.')

# One can also add in the keyword "not" to check a presence
cars = ['bugatti', 'honda', 'bmw', 'mercedes']
car = 'ford'
if car not in cars:
    print(f'{car.title()}, is not in the list.')
else:
    print(f'{car}, is in the list.')

# Addition of the elif into our if and else chain of conditionals 
age = 22
if age < 4:
    print('Your ticket is free.')
elif age < 18:
    print('Your ticket is $15.00')
else: 
    print('Your ticket is $25.00')

# A cleaner way to do this however
age = 15
if age <= 4:
    price = 0
elif age < 18:
    price = 15
else:
    price = 20
print(f'Welcome to the theme park your price is ${price}.')

# One can use as many elif blocks as they like
# For exmaple is a price was introduced for elders a new elif block could be added in for it 

age = 67

if age <= 4:
    price = 0

elif age > 65:
    price = 0

elif age < 18:
    price = 15

else:
    price = 20

print(f'The price for you is ${price}.')


# An else block if not always needed and does not have to be used, one may just use an elif block 
# else functions more as a catch all statement, but you can catch a particualr test instead with the elif statement too.

banned_users = ['alice', 'toby', 'john', 'leon']
user = 'alice'

if user in banned_users:
    print(f'{user.title()}, is banned.')
else:
    print(f'{user.title()}, is not banned.')

# Age checker to for addmision price
age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 15
elif age > 64:
    price = 0
elif age >= 18 and age <= 64:
    price = 20

print(f'Hello, welcome to the amusement park, your price today is, ${price}. Thank you.')

      
# When more than one condition could be true, we can use a series of if statements negating the else and elif blocks

requested_toppings = ['mushrooms', 'pineapple', 'mozarella', 'ham']
if 'mushroom' in requested_topping:
    print('Add mushrooms')
if 'peperoni' in requested_toppings:
    print('Add peperoni')
if 'ham' in requested_toppings:
    print('Add ham')
print('\nPizza finsihed')


squares = [value ** 2 for value in range(1, 11, 2)]
print(squares)

cubes = [value ** 3 for value in range(1, 11, 2)]
print(cubes)


requested_toppings = ['mushrooms', 'pineapple', 'mozarella', 'ham']
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print('NO MUSHROOMS')
    else:
        print(f'Adding, {requested_topping.upper()}.')
print('\nFinsihed making your pizza.')

# Checking for an empty list
# When the name of a list is used in an if statement python retruns True if the list has at least one item and flase if not
requested_toppings = ['mushrooms', 'pineapple', 'mozarella', 'ham']
if requested_toppings: 
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}, to your pizza.')
    else:
        print('Are you sure you want a plain pizza?!')

    

available_toppings = ('tomato', 'olives', 'salad', 'ham', 'sweetcorn', 'pineapple')
requested_toppings = ['tomato', 'fries', 'salad', 'ham']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Added {requested_topping.title()}.')
    else:
        print(f'Sorry, {requested_topping.title()}, is not available.')

print('\nYour Pizza is finsihed.')


# Creating a simple dictionary
alien_0 = {'colour': 'green' , 'points': 5}

new_points = alien_0['points']
print(f'You just earned {new_points} points.')

# Lets add some elements such as x and y positions to the dictionary of alien_0
print('\n',alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 10
print(alien_0)

# Starting with an empty dictionary and filling it
alien_1 = {}
print('\n',alien_1)

alien_1['colour'] = 'green'
alien_1['points'] = 5
alien_1['x_position'] = 0
alien_1['y_position'] = 10

print('\n',alien_1)

# One can change the value in a dictionary by simply redefining the value inside of it
print(f'The current colour of the alien is {alien_1["colour"]}')
alien_1['colour'] = 'yellow'
print(f'The alien has changed colour to {alien_1["colour"]}')

# Starting off with an empty dictionary
alien_0 = {}
alien_0['colour'] = 'blue'
alien_0['points'] = '5'
alien_0['x_position'] = 0
alien_0['y_position'] = 12
alien_0['speed'] = 'fast'
print(f'\nThe current set up of the Alien 0 is \n{alien_0}')

if alien_0['speed'] == 'slow':
    x_increment = 2
if alien_0['speed'] == 'medium':
    x_increment = 4
if alien_0['speed'] == 'fast':
    x_increment = 6

alien_0['x_position'] = x_increment + alien_0['x_position']
print(f'\nNew position: {alien_0["x_position"]}')


alien_2 = {'colour': 'blue', 'points': 5, 'speed': 'fast'}

# A key value pair in the dictionary can be removed using the del statement 
del alien_0['points']
print(alien_0)


favourite_languages = {
    'chiara': 'html',
    'toby': 'java',
    'tadhg': 'python',
    'jim': 'css',
}
print(f"Chiara's favourite language is, {favourite_languages['chiara'].upper()}")


# Using keys in square brackets is fine however if the ket is nonexistent it will result in a traceback error
# Therefore alternatively we could use the 'get' method
# The get method requires a key as its first argument as a second optional argument a value of return can be placed 

alien_0 = {'colour': 'green', 'points': '5', 'speed': 'slow'}
alien_position = alien_0.get('alien_position', 'alient position not available')
print(alien_position)
alien_colour = alien_0.get('colour', 'Colour not in dictionary')
print(alien_colour)

alien_0 = {}
alien_0['colour'] = 'green'
alien_0['points'] = '5'
alien_0['position'] = 2
alien_0['speed'] = 'medium'

print(alien_0)

if alien_0['speed'] == 'slow':
    increment = 2
if alien_0['speed'] == 'medium':
    increment = 4
if alien_0['speed'] == 'fast':
    increment = 6

print(f"Alien 0's posiion is {increment + alien_0['position']}.")


# Creating a simple dictionary from memory 

bob = {'hair': 'brown', 'eyes': 'green', 'height': 'tall'}
print(bob['eyes'].title())

# Creating a long dictionary from memory 

favourite_languages = {
    'chiara': 'html',
    'tadhg': 'python',
    'dan': 'golang',
    }

print(favourite_languages['dan'].title() , favourite_languages['tadhg'].title() , favourite_languages['chiara'].upper())

# Lets now chuck in some use of the get method

print(favourite_languages.get('chiara', 'Chiara Not Returned').upper())
chiara_language  = favourite_languages.get('chiara', 'Chiara Value Not Returned').upper()
print(chiara_language)

# If there is a chance the key you're looking for does not exist the use the get method as the function will result 
# in a traceback error.

# Lets now look as to how we can loop through a dictionary
# First lets create a dictionary of a user

user_0 = {
    'username': 'tsavage',
    'first_name': 'tadhg',
    'surname': 'savage',
}

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')
print('\nThese are the keys and valus for your user.')


# Below will work only for keys as a dictionary will iterate in order hence the necesity to use the .items() method
# which will iterate again over the second colomn in the dictionary.

for key in user_0:
    print(f'\nKey: {key}')

for value in user_0:
    print(f'\nValue: {value}')

# Test case for user_1 written again.

user_1 = {
    'username': 'cpresaghi',
    'forename': 'chiara',
    'surname': 'presaghi',
}

for key, value in user_1.items():
    print(f'\nKey: {key.upper()}')
    print(f'Value: {value}')
print('These are the keys and values.')

# Lets now recreate this dictionary and loop for the favourite languages

favourite_languages = {
    'john': 'java', 
    'cena': 'html', 
    'tadhg': 'python', 
    'chiara': 'css',
}

for key, value in favourite_languages.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')
print('These are peoples favourite langauges.')

for name, language in favourite_languages.items():
    print(f'{name.title()}, favourite language is {language}.')





