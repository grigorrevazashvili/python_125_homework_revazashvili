#Homework 5 Task 2

def count_letters(text):
    counts = {}
    text = text.lower()

    for char in text:
        if char != " ":
            if char in counts:
                counts[char] +=1
            else:
                counts[char] = 1
    return counts

result = count_letters("Hello World")
print(result)
