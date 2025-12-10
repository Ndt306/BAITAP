print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

class Bank:
    Account_type = "Savings"
    location = "Guntur"
    def __init__(self, name, Account_Number,balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location
    def __repr__(self):
        print("Welcome to the SBT ATM Machine ")
        print("------------------------------ ")
        account_pin = int(input("Please enter your pin number"))
        if(account_pin==123):
            Account(self)
        else:
            print("Pin Incorrect. Please try again")
            Error(self)
        return ' '.join([self.name,self.Account_Number])

def Error(self):
    account_pin = int(input("Please enter your pin number"))
    if(account_pin==123):
        Account(self)
    else:
        print("Pin Incorrect. Please try again")
        Error(self)
def Account(self):
    print("Your Card Number is:XXX XXX XXX")
    print("Would you like to deposit/withdraw/Check Balance?")
    print("""
1)        Balance
2)        With
3)        Deposit
4)        Quit
""")
    option =int(input("Please enter your choice:"))
    if(option==1):
        Balance(self)
    elif(option==2):
        Withdraw(self)
    elif(option==3):
        Deposit(self)
    elif(option==4):
        exit()
def Balance(self):
    print("Balance:",self.balance)
    Account(self)
def Withdraw(self):
    w=int(input("Please Enter Desired amount: "))
    if(self.balance>0 and self.balance>=w):
        self.balance=self.balance-w
        print("Your transaction is successfull")
        print("Your Balance:",self.balance)
        print("")
    else:
        print("Your transaction is cancelled due to")
        print("Amount is not sufficient in your account")
    Account(self)
def Deposit(self):
    d=int(input("Please enter desired amount:"))
    self.balance=self.balance+d
    print("Your transaction is successfull")
    print("Balance:",self.balance)
    Account(self)
def Exit():
    print("Exit")
T1 = Bank('mahesh',1453210145,5000)

print(T1)
        
