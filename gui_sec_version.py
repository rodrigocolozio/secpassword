#import
import random
import time
import string
import tkinter as tk

# creatin GUI
def show_new_password_screen():
    # Hide the current screen
    welcome_frame.pack_forget()
    
    # Show the new password screen
    new_password_frame.pack()

def show_fortify_password_screen():
    # Hide the current screen
    welcome_frame.pack_forget()
    
    # Show the fortify password screen
    fortify_password_frame.pack()

# implementing my logic method
def new_password_method():
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    password = []

    for l in range(1, int(letters_count.get()) +1):
        password.append(random.choice(letters))
        

    for s in range(1, int(symbols_count.get()) + 1):
        password.append(random.choice(symbols))

    for n in range(1, int(numbers_count.get()) + 1):
        password.append(random.choice(numbers))


    random.shuffle(password)
    final_password = ''.join(password)


    password_label.config(text=f'Your unique generated password i: {final_password}')
    print(f'Your unique generated password is: {final_password}')

def generate_current_password():
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    password = []
    password.append(password_entry.get())

    for _ in range(1, int(add_symbols.get()) + 1):
        password.append(random.choice(symbols))

    for _ in range(1, int(add_numbers.get()) + 1):
        password.append(random.choice(numbers))

    random.shuffle(password)
    final_password = ''.join(password)

    new_fortified_label.config(text=f'Your current fortified password is: {final_password}')
    # FINALIZAR


# Create the main application
app = tk.Tk()
app.title('SecPassword - Secure Generator')
app.geometry("720x480")

# Welcome Screen
welcome_frame = tk.Frame(app)
welcome_frame.pack()

welcome_title = tk.Label(welcome_frame, text="Welcome to SecPassword", font=("Arial", 20))
welcome_title.config(pady=20)
welcome_title.pack()
subtitle = tk.Label(welcome_frame, text="A secure way to generate passwords.", font=('Arial', 14))
subtitle.config(pady=15)
subtitle.pack()

button1 = tk.Button(welcome_frame, text='New Password', command=show_new_password_screen)
button1.pack()

button2 = tk.Button(welcome_frame, text='Fortify your current password', command=show_fortify_password_screen)
button2.pack()

# New Password Screen
new_password_frame = tk.Frame(app)
first_questions = tk.Label(new_password_frame, text="How many letters would you like in your password?")
first_questions.config(pady=10)
first_questions.pack()
letters_count = tk.Entry(new_password_frame)
letters_count.pack()

second_question = tk.Label(new_password_frame, text="How many symbols would you like in your password?")
second_question.pack()
symbols_count = tk.Entry(new_password_frame)
symbols_count.pack()

third_question = tk.Label(new_password_frame, text="How many numbers would you like in your password?")
third_question.pack()
numbers_count = tk.Entry(new_password_frame)
numbers_count.pack()

generate_new_password_button = tk.Button(new_password_frame, text="Generate New Password", command=new_password_method, bg="blue")
generate_new_password_button.pack()

# result label 
password_label = tk.Label(new_password_frame, text="", font=('Arial', 12))
password_label.pack()


# Fortify Password Screen
fortify_password_frame = tk.Frame(app)
fourth_questions = tk.Label(fortify_password_frame, text="Enter your current password")
fourth_questions.pack()
password_entry = tk.Entry(fortify_password_frame)
password_entry.pack()

fifth_question = tk.Label(fortify_password_frame, text="How many symbols would you like to add?")
fifth_question.pack()
add_symbols = tk.Entry(fortify_password_frame)
add_symbols.pack()
last_question = tk.Label(fortify_password_frame, text="How many numbers would you like to add?")
last_question.pack()
add_numbers = tk.Entry(fortify_password_frame)
add_numbers.pack()
generate_fortified_password_button = tk.Button(fortify_password_frame, text="Fortify your password", command=generate_current_password ,background="blue")
generate_fortified_password_button.pack()
new_fortified_label = tk.Label(fortify_password_frame, text='')
new_fortified_label.pack()

# Add widgets for the fortify password screen here

# Initially, show the welcome screen
app.mainloop()
show_new_password_screen()
show_fortify_password_screen()











#_____________________________________________

# logic of my main code woring on terminal
def new_password():

    letters_count = int(input('How many letter do you want in your password?\n'))
    simbols_count = int(input('How many simbols do you want in your password?\n'))
    numbers_count = int(input('How many numbers do you want in your password?\n'))

    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    simbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    password = []

    for l in range(1, letters_count +1):
        password.append(random.choice(letters))
        

    for s in range(1, simbols_count + 1):
        password.append(random.choice(simbols))

    for n in range(1, numbers_count + 1):
        password.append(random.choice(numbers))


    random.shuffle(password)
    final_password = ''.join(password)
    print(f'Your unique generated password is: {final_password}')

def generate_existent_password():

    letters_count = input('What is the password that you want to fortify?\n')
    simbols_count = int(input('How many simbols do you want in your password?\n'))
    numbers_count = int(input('How many numbers do you want in your password?\n'))

    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    simbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    password = []
    password.append(letters_count)
    print(password)

    for s in range(1, simbols_count + 1):
        password += random.choice(simbols)

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
print('Adivce: choose a password with at least 8 character!\n\n\n')
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




