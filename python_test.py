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
message = (f"The last car i owned was a, {last_car.title()}.")
print(message)




