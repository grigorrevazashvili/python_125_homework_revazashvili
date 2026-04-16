#Homework 3.4

#Task 4

attempts=0

while attempts<3:
    password=input("Enter password: ")

    if password == "python123":
        print("Correct! Access granted!")
        break
    else:
        attempts+=1
        if attempts == 3:
            print("Account locked!")
        else:
            print("Wrong password, try again.")
