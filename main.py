import string
import random

letters = list(string.ascii_letters) 
digits = list(string.digits)
punctuation = list(string.punctuation)


def user_input():
    incorrect_input = True

    while incorrect_input:
        lenght = int(input("How long should be the password? "))
        no_digits = int(input("How many digits should be in the password? "))
        no_punctuation = int(input("How many punctuation should be in the password? "))

        if no_digits + no_punctuation <= lenght:
            incorrect_input = False
            return lenght, no_digits, no_punctuation
        else: print("no cheating!")

def password_generator(letters, digits, punctuation, *args):
    password = ''
    no_letters = args[0][0] - args[0][1] - args[0][2]
    for l in range(0, no_letters):
        char = random.randint(0, len(letters)-1)
        password += letters[char]

    for d in range(args[0][1]):
        char = random.randint(0, len(digits)-1)
        password += digits[char]

    for p in range(args[0][2]):
        char = random.randint(0, len(punctuation)-1)
        password += punctuation[char]
    
    return password

def shuffling_password(password):
    final_password = ''.join(random.sample(password,len(password)))
    return final_password


user_inputs = user_input()
password = password_generator(letters, digits, punctuation, user_inputs)
final_password = shuffling_password(password)
print(final_password)