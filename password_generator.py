import random
import string

def generate_random_password():
    # Definimos los caracteres ha utilizar / We define the characters we will use.
    numbers = [str(random.randint(1, 99)) for _ in range(4)]
    uppercase_letters = [random.choice(string.ascii_uppercase) for _ in range(2)]
    lowercase_letters = [random.choice(string.ascii_lowercase) for _ in range(2)]
    special_characters = [random.choice('!@#$%^&*()-_=+\|{};:/?') for _ in range(3)]

    # Combinamos todos los sets de caracteres / We combine all sets of characters
    all_characters = numbers + uppercase_letters + lowercase_letters + special_characters

    # Mezclamos los caracteres combinados (largo=15) / We shuffle the combined characters (legth=15)
    random.shuffle(all_characters)

    # Unimos los caracteres para formar la contraseña / We join all characters together
    password = ''.join(all_characters)

    return password 

def main():
    print('ᴍᴀᴅᴇ ʙʏ ɪᴠᴏ ᴅᴀɴᴋᴏ')
    while True:
        password = generate_random_password()
        print(f"Generated Password: {password}")

        iteration = input("Do you want to generate another password? (YES/NO): ")
        if iteration != 'yes':
            break

if __name__ == "__main__":
    main()

# Contraseñas posibles (aproximadas)/possible amount of passwords(roughly): 
