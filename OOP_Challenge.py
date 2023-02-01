

# Bank Account

class Account():

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"

    def deposit(self,dollars):
        print(f"Deposit Processed of {dollars}")
        self.balance = self.balance+dollars

    def withdraw(self,dollars):

        if self.balance >= dollars:
            print(f"Withdraw Processed of {dollars}")
            self.balance = self.balance-dollars
        else:
            print("Insufficient Funds")
            print(f"Could not process withdraw of {dollars}")


acct1 = Account('Chris',1000)

print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
print(acct1.balance)
acct1.withdraw(1000)
print(acct1.balance)
acct1.withdraw(100)
print(acct1.balance)




