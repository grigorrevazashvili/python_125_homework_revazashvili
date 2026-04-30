#Homework 7



#Task 3

class Bankaccount:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        if amount<0:
            print ("A deposit amount must be positive")
        else:
            self.balance+=amount
    def withdraw(self, amount):
        if amount<0:
            print("Cannot withdraw a negative amount")
        elif amount>self.balance:
            print("Not enough funds")
        else:
            self.balance-=amount

            
    def __str__(self):
        return f"Account({self.owner}): ${self.balance}"
    
account = Bankaccount("Giga")

account.deposit(300)
account.withdraw(10)
account.withdraw(20)
account.withdraw(50)
account.withdraw(600)

print(account)
                        

