#Homework 3.3

#Task 3

evens=[]
odds=[]

for number in range(1,21):
    if number%2==0:
        evens.append(number)
    else:
        odds.append(number)

print("Even numbers:", evens)
print("Odd numbers:",odds)