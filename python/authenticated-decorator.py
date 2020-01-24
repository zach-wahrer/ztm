# Create an @authenticated decorator that only allows the function to run is
# user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}
user2 = {
    'name': 'Gerry',
    'valid': False  # changing this will either run or not run the message_friends function.
}


def authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return function(*args, **kwargs)
        else:
            return print(f'Sending not authorized for {args[0]["name"]}')
    return wrapper


@authenticated
def message_friends(user):
    print(f'Message has been sent for {user["name"]}')


message_friends(user1)
message_friends(user2)
