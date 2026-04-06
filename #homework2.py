#homework2
#Task#1

name=input("Enter your name: ")

print("UPPERCASE:", name.upper())
print("lowercase:", name.lower())
print("Title Case:", name.title())

#Task#2

sentence=" the quick brown fox jumps over the lazy dog "
stripped_sentence=sentence.strip()

print("Stripped:", stripped_sentence)
print("Count of'o':",stripped_sentence.count("o"))
print("Replaced:",stripped_sentence.replace("fox","cat"))

words=stripped_sentence.split()
print("First 3 words:", words[:3])

#Task#3

age=int(input("Enter your age:"))

if age<0:
    print("Invalid age!")
elif age<13:
    print("You are a child.")
elif age<=17:
    print("You are a teenager.")
elif age<=64:
    print("You are an adult")
else:
    print("You are a senior.")

#Task 4
username = input("Enter username: ")
password = input("Enter password: ")

if username=="admin":
    if password=="secret":
        print("Welcome,Admin!")
    else:
        print("Incorrect password.")
else:
    print("User not found.")

#Task 5

age=int(input("Enter your age:"))
student=input("Are you a student? (yes or no):").lower()

if age<12:
    price=5
elif age>=65:
    price=10
elif student == "yes":
    price =8
else:
    price=15

print (f"Ticket price: ${price}")