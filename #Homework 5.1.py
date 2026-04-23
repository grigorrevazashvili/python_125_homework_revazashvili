#Homework 5 Task 1 

grades ={
    "Alice": 88,
    "Carl": 74,
    "Charlie": 95,
    "Diana":87,
    "Nick":79
}

for student, score in grades.items():
    print(f"{student}: {score}")

average = sum(grades.values())/len (grades)
print("Class average:", round(average,2))

top_student=max(grades, key=grades.get)
print("Highest-scorung student:", top_student, "-", grades[top_student])