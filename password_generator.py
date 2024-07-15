from tkinter import * 
import random
import string

root = Tk()
root.title('Password Generator!')
root.geometry('400x200')

def generate_random_password():
    numbers = [str(random.randint(1, 99)) for _ in range(4)]
    uppercase_letters = [random.choice(string.ascii_uppercase) for _ in range(2)]
    lowercase_letters = [random.choice(string.ascii_lowercase) for _ in range(2)]
    special_characters = [random.choice('!@#$%^&*()-_=+|{};:/?') for _ in range(3)]

    all_characters = numbers + uppercase_letters + lowercase_letters + special_characters

    random.shuffle(all_characters)

    password = ''.join(all_characters)

    return password 

def generate_password():
    password = generate_random_password()
    show_password.config(text=password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(show_password.cget("text"))
    root.update()
    copied_label.config(text="Password copied!")

show_password = Label(root, text="", font=('Helvetica', 14))
show_password.pack(pady=10)

generate_button = Button(root, text='Generate password', command=generate_password)
generate_button.pack(pady=10)

copy_button = Button(root, text='Copy to Clipboard', command=copy_password)
copy_button.pack(pady=10)

copied_label = Label(root, text="", font=('Helvetica', 10))
copied_label.pack(pady=5)

root.mainloop()











"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
··························································
: __  __           _        _             ___            :
:|  \/  | __ _  __| | ___  | |__  _   _  |_ _|_   _____  :
:| |\/| |/ _` |/ _` |/ _ \ | '_ \| | | |  | |\ \ / / _ \ :
:| |  | | (_| | (_| |  __/ | |_) | |_| |  | | \ V / (_) |:
:|_|__|_|\__,_|\__,_|\___| |_.__/ \__, | |___| \_/ \___/ :
:|  _ \  __ _ _ __ | | _____      |___/                  :
:| | | |/ _` | '_ \| |/ / _ \                            :
:| |_| | (_| | | | |   < (_) |                           :
:|____/ \__,_|_| |_|_|\_\___/                            :
··························································
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

