import time

username = 'dinma'
password = 'secretpassword'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access granted')
    print('Please wait')
    time.sleep(1)
    print('...')
    print('Alright you have security clearance, Pulling up the secret mainframe.')
    print('Now.. Loading..')
elif username_input == username and password_input != password:
    print('Access Declined')
elif username_input != username and password_input == password:
    print('Access Declined')
else:
    print("Check both fields again, Please...") 