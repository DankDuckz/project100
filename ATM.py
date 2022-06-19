class ATM(object):
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is: $0.01")
    
    def withdraw(self,amount):
        print("You've withdrawn: $" + str(amount))

    def deposit(self,amount):
        print("You've deposited: $" + str(amount))

atm = ATM(1001001000,1234)
atm.checkBalance()
atm.withdraw(1000)
atm.deposit(10000000)