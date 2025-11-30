import random
import string

letters = string.ascii_letters
numbers = string.digits

def generate_string(length):
    result = ""

    for i in range(length):
        letter_or_digit = random.randint(0, 1)
        choice = random.choice(letters) if letter_or_digit == 1 else random.choice(numbers)
        result = result + choice
    
    print(result)


while True:
    usr_input = input()
    quits = ["q", "Q", "quit", "Quit", "QUIT"]
    if usr_input in quits:
        break
    else:
        generate_string(int(usr_input))