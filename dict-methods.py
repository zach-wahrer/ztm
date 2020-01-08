# Scroll down to see the answers!
# 1 Create a user profile for your new game. This user profile will be stored in
# a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age': 35,
    'username': 'zerowolf',
    'weapons': None,
    'is_active': True,
    'clan': 'wolf'
}
# 2 iterate and print all the keys in the above user.
print(list(user_profile.keys()))
# 3 Add a new weapon to your user
user_profile.update({'weapons': 'knife'})
# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})
# 5 Ban the user by setting the previous key to True
user_profile.update({'is_banned': True})
# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({'username': 'Jerry', 'age': 10})

print(user_profile)
print(user2)
