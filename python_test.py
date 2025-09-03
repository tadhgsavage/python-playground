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








      

      




