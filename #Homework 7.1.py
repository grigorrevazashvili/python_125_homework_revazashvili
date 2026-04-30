#Homework 7


#Task 1


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p1 = Person("Carl", 43)
p2 = Person("Mike", 29)
p3 = Person("Nick", 15)

p1.greet()
p2.greet()
p3.greet()
