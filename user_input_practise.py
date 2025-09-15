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
        'location': 'roma',
    }
}

for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    email = user_info['email']
    location = user_info['location']

    print(f"\tName: {full_name.title()}")
    print(f"\tEmail: {email}")
    print(f"\tLocation: {location.title()}")
