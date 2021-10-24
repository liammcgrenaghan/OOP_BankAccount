#!/bin/python3.5


class Account: 
    limit = -1000
    class_name = "Account"

    #optional parameters
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount

    def __str__(self):
        return "{} ('{}',{})"\
                .format(self.class_name,\
                        self.owner,self.amount)

    def withdraw(self,howmuch):
        new_amount = self.amount - howmuch 
        if new_amount < self.limit:
            print("sorry, over limit")
        else:
            self.amount = new_amount

    def deposit(self,howmuch):
        self.amount += howmuch 

    def statement(self):
        return "Owner : {}, amount : {}"\
                .format(self.owner, self.amount)


class savingsAccount(Account):
    interest_rate = 0.05

    class_name = "savingsAccount"
    
    def add_interest(self):
        self.deposit(self.amount * self.interest_rate)

    def withdraw(self,howmuch):
        if self.amount - howmuch < 0:
            print("Savings accounts cannot be overdrawn")
        else:
           super(savingsAccount,self).withdraw(howmuch)
