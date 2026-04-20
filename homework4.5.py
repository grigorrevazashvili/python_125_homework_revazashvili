#Homework 4, Task 5

def letter_grade(score):
    if score >=90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"

def class_report(grades):
    for score in grades:
        print (f"Score: {score} -> Grade: {letter_grade(score)}")
    print("Class average:", round(sum(grades) / len(grades), 2))

grades = [92, 85, 67, 74, 55, 91, 80]
class_report(grades)
    

    


