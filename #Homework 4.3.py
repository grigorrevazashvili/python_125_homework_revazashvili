#Homework 4 Task 3

def list_stats(numbers):
    total = sum(numbers)
    average = total/len(numbers)
    smallest = min(numbers)
    largest = max(numbers)
    return total, average, smallest, largest

numbers = [10,30,4,45,15,33,7]

total, average, smallest, largest = list_stats(numbers)

print("Sum:", total)
print("Average:", average)
print("Smallest:", smallest)
print("Largest:", largest)