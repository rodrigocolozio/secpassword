import random
import time
import string


#option one - choose a new generated password

def new_password():

    letters_count = int(input('How many letters do you want in your password?\n'))
    symbols_count = int(input('How many symbols do you want in your password?\n'))
    numbers_count = int(input('How many numbers do you want in your password?\n'))

    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    password = []

    for l in range(1, letters_count +1):
        password.append(random.choice(letters))
        

    for s in range(1, symbols_count + 1):
        password.append(random.choice(symbols))

    for n in range(1, numbers_count + 1):
        password.append(random.choice(numbers))


    random.shuffle(password)
    final_password = ''.join(password)
    print(f'Your unique generated password is: {final_password}')

def generate_existent_password():

    letters_count = input('What is the password that you want to fortify?\n')
    symbols_count = int(input('How many symbols do you want in your password?\n'))
    numbers_count = int(input('How many numbers do you want in your password?\n'))

    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    password = []
    password.append(letters_count)
    print(password)

    for s in range(1, symbols_count + 1):
        password += random.choice(symbols)

    for n in range(1, numbers_count + 1):
        password += random.choice(numbers)


    random.shuffle(password)
    final_password = ''.join(password)
    print(f'Your fortified password is: {final_password}')




print(''' 
 _____          ______                                   _ 
/  ___|         | ___ \                                 | |
\ `--.  ___  ___| |_/ /_ _ ___ _____      _____  _ __ __| |
 `--. \/ _ \/ __|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` |
/\__/ /  __/ (__| | | (_| \__ \__ \\ V  V / (_) | | | (_| |
\____/ \___|\___\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                                                           
                                                           
''')
print('Welcome to SecPassword, a secure password generator.\nTo continue, please answer the questions bellow about how you would like your password to be\n\n\n')
print('Advice: choose a password with at least 8 character!\n\n\n')
time.sleep(2)
print('Choose how you want to continue:\n1 - New password\n2 - Generate a new password from your own')
method_choice = int(input('> '))
time.sleep(2)

if method_choice == 1:
    print('You have chose New Password.')
    new_password()
elif method_choice == 2:
    print('You have chose Generate a new password from your own.')
    generate_existent_password()
else:
    print('Invalid number. Please select a number between 1 or 2.')




