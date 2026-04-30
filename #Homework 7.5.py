#Homework 7

#Task 6

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self):
        return f"Book({self.title},{self.author},{self.pages}p)"
    
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author
    
    def __len__(self):
        return self.pages
    
book1 = Book("Harry Potter", "J.K.Rowling",300)
book2 = Book("Harry Potter", "J.K.Rowling", 320)
book3 = Book("Troy","Homer",60)

print(book1)
print(book2)
print(book3)

print(book1 == book2)
print(book1 == book3)

print(len(book1))
print(len(book3))


    