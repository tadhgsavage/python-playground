favourite_languages = {
    'toby': 'java',
    'chiara': 'html',
    'tadhg': 'python',
    'dan': 'golang',
    'jemma': 'c',
}

favourite_friends = ['tadhg', 'chiara']

if 'erin' not in favourite_friends:
    print('Erin, please take our poll.')

# One can also loop thorugh a dictionaries keys in a particular order

favourite_languages = {
    'toby': 'python',
    'tadhg': 'html',
    'euan': 'java',
    'chiara': 'css',
}

for key in (sorted(favourite_languages.keys())):
    print(f'Hi, {key.title()}')

# Printing out of all of the langages in alphabetical order

print('The following languages have been mentioned:')
for language in (sorted(favourite_languages.values())):
    print(language.title())


# Identifying duplicates making a collection using the function "set"
# If the list was long and one wanted to remove duplicates one can use the function set to achieve this

favourite_languages = {
    'toby': 'python',
    'tadhg': 'html',
    'euan': 'java',
    'chiara': 'css',
    'john': 'python',
    'kobi': 'html',
}


print('Here are the choice of all languages:')
# This removes duplictaes and sorts in alphabetical order
for langauge in (set(sorted(favourite_languages.values()))):
    # Looks for if html and css exist and if they do they print them to upper 
    if langauge == 'html' or langauge == 'css':
        print(langauge.upper())
    # For all other languegs the get printed to title case only
    else:
        print(langauge.title())


# One can also use set on a list to quickly remove duplicates, order does not matter
# Due to hasing the order for sets is fairly random (not truly, but fairly)
cars = ['bugatti', 'bmw', 'ford', 'ford', 'honda']
print(set(cars))

# One can cal the sorted function which will put the printed set into alphabetical order such as here below
cars = ['bugatti', 'bmw', 'ford', 'ford', 'honda']
print(sorted(set(cars)))

# Nesting
# Nesting multiple dicitonaries inside of a list 

# Creating a simple dictionary of each alien
alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'red', 'points': 10}
alien_2 = {'colour': 'yellow', 'points': 2}

# Creating a list of which inside is the dictionary of each alien
aliens =[alien_0, alien_1, alien_2]
print(aliens)

# Or one can loop through the list to print out each alien
for alien in aliens:
    print(alien)


# Lets make some code that will automatically generate 30 aliens to put inside of a dictionary nested in a list 

# First lets start off with an empty list of aliens
aliens = []
# Make 30 identical green aliens
# Here the range fucntion returns a series of numbers telling python how many times we want the loop the repeat, each repeat is a new alien
for alien_number in range(30):
    # The loop is ran 30 times so we create a 'new alien' as described below 30 times
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    # Each 'new alien' is then appened to the empty list of aliens
    aliens.append(new_alien)

# We can now use a loop and a slice to print out the first 5 aliens to prove
for alien in aliens[:5]:
    print(alien)

# To prove that we have indeed generated 30 aliens we can print out the length of the list of aliens
print(f'There is a total {len(aliens)} Aliens')

# All of these 30 aliens are identical however they are also seperate objects which allows for individual modification of each
# So lets now change the first three aliens colour, speed and points and print out the first five aliens
# As we want to modify only the first three, we loop through the first three using a slice 
for alien in aliens[:3]:
    # If statement is used as although they are green now that wont always be the case and we only want to modify green aliens
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
# The program could be extended with an elif block to make yellow ones red 
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
# Loop through the first 5 aliens and print out their colour
for alien in aliens[:5]:
    print(alien)

# The program could be extended with an elif block to make yellow ones red 


pizzas =[]
for replicated_pizza in range(30):
    new_pizza = {'type': 'diavola', 'crust': 'thin'}
    pizzas.append(new_pizza)
for pizza in pizzas:
    print(pizza)


# Now lets create a list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['tomatoes', 'salami', 'mozzarella', 'onion'],
}
print(f'You have ordered a {pizza["crust"]} crust with:')
for topping in pizza['toppings']:
    print(f'{topping}')

favourite_pizzas = {
    'tom': ['diavola', 'peperoni'],
    'tadhg': ['margherita', 'sloppy guisepe'],
    'chiara': ['marinara', 'diavola'],
}

for names, pizzas in favourite_pizzas.items():
    print(f'{names.title()}, favourite pizza is:')
    for pizza in pizzas:
        print(pizza.title())
    

# Creating a quick list inside of a dictionary and printing out with styling

favourite_languages = {
    'tadhg': ['python', 'java'],
    'chiara': ['html', 'css', 'go'],
    'toby': ['django', 'c'],
}

for names, languages in favourite_languages.items():
    print(f"{names.title()}'s favourite languages are:")
    for language in languages:
        if language.lower() in {'html', 'css', 'c'}:
            print(f'\t{language.upper()}')
        else:
            print(f'\t{language.title()}')


# Creating a dictionary inside of a dictionary

users = {
    'tsavage': {
        'first': 'tadhg',
        'last': 'savage',
        'email': 'tadhgsavage@gmail.com',
        'location': 'kent',
        },
    'cpresaghi': {
        'first': 'chiara',
        'last': 'presaghi',
        'email': 'chiara.presaghi@gmail.com',
        'location': 'rome',
        },
    }

for username, user_info in users.items():
    print(f'Username: {username}')
    full_name = (f"{user_info['first']} {user_info['last']}")
    email = user_info['email']
    location = user_info['location']
    
    print(f'\t{full_name.title()}')
    print(f'\t{email}')
    print(f'\t{location.title()}')


