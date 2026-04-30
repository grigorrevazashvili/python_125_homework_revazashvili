#Homework 7

#Task 4

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

animal = Animal("Buddy")
dog = Dog("Rex")
cat = Cat("Kitty")

animals = [animal, dog, cat]

for a in animals:
    a.speak()



