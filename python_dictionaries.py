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

print('The following languages have been mentioned:')
for lanhuage in (sorted(favourite_languages.values())):
    print(lanhuage.title())

