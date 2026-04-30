#Homework 7

#Task 2

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return (2*self.width)+(2*self.length)
    
    def is_square(self):
        return self.width==self.length
    

r = Rectangle(6,9)
print (r.area())
print (r.perimeter())
print (r.is_square())

s = Rectangle(2,2)
print (s.is_square())

