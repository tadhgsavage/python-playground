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








    

