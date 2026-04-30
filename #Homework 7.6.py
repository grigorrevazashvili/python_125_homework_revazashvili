#Homework 7

#Task 6 

class Student:
    def __init__(self,name):
        self.name = name
        self.grades =[ ]
    
    def add_grade(self,grade):
        self.grades.append(grade)
    
    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades)/ len(self.grades)
    
    def __repr__(self):
        return f"Student ({self.name})"

class Course:
    def __init__(self,name):
        self.name = name
        self.students = []
    
    def enroll(self,student):
        self.students.append(student)
    
    def class_average(self):
        if len(self.students) == 0:
            return 0
        total = 0
        for student in self.students:
            total+= student.average()
        return total/len(self.students)
    
    def top_student(self):
        if len(self.students)==0:
            return None
        return max(self.students, key=lambda student: student.average())

s1 = Student("Alice")
s1.add_grade(95)
s1.add_grade(87)
s1.add_grade(83)

s2 = Student("Carl")
s2.add_grade(73)
s2.add_grade(75)
s2.add_grade(76)

s3 = Student("Mickey")
s3.add_grade(94)
s3.add_grade(76)
s3.add_grade(79)

course = Course("Spanish")
course.enroll(s1)
course.enroll(s2)
course.enroll(s3)

print("Class average:", round(course.class_average(), 2))
print("Top student:", course.top_student().name)
print("Top student average:", round(course.top_student().average(),2))
