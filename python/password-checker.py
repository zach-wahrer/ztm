username = input('Username: ')
password = input('Password: ')

password_length = len(password)
obscured_password = '*' * password_length

print(f'{username}, your password [{obscured_password}] is {password_length}' +
      ' characters long.')
