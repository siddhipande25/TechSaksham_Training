class Bank:
    
    def __init__(self,amt):
        self.amt = amt
    def deposite(self,depo):
        self.amt += depo
        print(f'the depo {depo} credited in your bank and total balance is {self.amt}')
    def withdraw(self,withdraw):
        self.amt -= withdraw
        print(f'the withdraw {withdraw} debited in your bank and total balance is {self.amt}')
    def show(self):
        print(f'Total available balance is {self.amt}')
obj = Bank(10)
obj.deposite(110)
obj.withdraw(50)
obj.show()