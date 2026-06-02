import random
import string
import time
import sys
from termcolor import colored


print(colored("""
     ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄      ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓    ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒      ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░    ░ ░   ░    ░      ░   ░ ░ 
               ░  ░      ░        ░      ░        ░ ░     ░        ░             ░    ░  ░         ░ 
                                                                 ░                                   
                                                                 """, "blue"))



answer = input(colored('How many passwords do you want to generate?', "green"))
answer = int(answer)

answer2 = input(colored('How many characters long does your password need to be?', "green"))
answer2 = int(answer2)

# Function to generate a random password
def generate_password():
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for i in range(answer2))
    return password

for i in range(answer):
    password = generate_password()
    print(colored(f"Generated Password {i + 1}: {password}", "blue"))
    time.sleep(0.1)



# Countdown before exit
def countdown():
    for i in range(5, 0, -1):
        print(colored(f"Exiting in {i} seconds...", "red"))
        time.sleep(1)  # Wait for 1 second
    print("Goodbye!")
    sys.exit()

countdown()
