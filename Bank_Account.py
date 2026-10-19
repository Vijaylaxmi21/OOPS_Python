class BankAccount:
    def __init__(self,account_number , owner_name,balance):
        self.account_number = account_number 
        self.owner_name = owner_name
        self.balance = balance 
    def deposit(self,amount):
        self.balance += amount
        print("Amount deposited=",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Amount withdrawn:",amount)
        else:
            printf("Insufficient balance")
    def check_balance(self):
        print("Current balance = ",self.balance)

account=BankAccount(100,"Aryan",1000000)

account.deposit(200000)
account.withdraw(100000)
account.check_balance()
