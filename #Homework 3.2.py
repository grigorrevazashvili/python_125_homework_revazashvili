#Homework 3.2

#Task 2

numbers=[]

for i in range(5):
    number=float(input("Enter a number: "))
    numbers.append(number)

print("List of numbers:",numbers)
print("Sum:", sum(numbers))
print("Average:", sum(numbers)/len(numbers))
print("Largest number:", max(numbers))
print("Smallest number", min(numbers))