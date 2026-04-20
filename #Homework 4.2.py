#Homework 4, Task 2

def circle_area(radius):
    return 3.14159 * radius * radius

def circle_circumference(radius):
    return 2 * 3.14159 * radius

def circle_info(radius):
    area= circle_area(radius)
    circumference=circle_circumference(radius)
    return area, circumference

area, circumference = circle_info(5)

print("Area:", area)
print ("Circumference:", circumference)
