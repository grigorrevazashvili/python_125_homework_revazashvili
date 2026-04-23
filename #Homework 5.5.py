#Homework 5.5

class_a = ["Inception", "Matrix", "Interstellar", "Joker", "Matrix"]
class_b = ["Matrix", "Titanic", "Joker", "Avatar", "Titanic"]

set_a = set(class_a)
set_b = set(class_b)

both = set_a & set_b
only_one = set_a ^ set_b
total_distinct = len(set_a | set_b)

print("Movies liked by BOTH classrooms:", both)
print("Movies liked by only ONE classroom:",only_one)
print("Total number of distinct movies:", total_distinct)