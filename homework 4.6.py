#Homework 4 Task 6

import random

def generate_password(length=12, use_digits=True, use_uppercase=True):
    characters = "abcdefghijklmnopqrstuvwxyz"

    if use_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if use_digits:
        characters += "0123456789"
    
    password = " "

    for i in range(length):
        password += random.choice(characters)

    return password

print(generate_password())
print(generate_password(8))
print(generate_password(16, use_digits=False))

