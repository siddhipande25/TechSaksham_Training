class Bank:
    
    def __init__(self):
        self.details = {'user1':{1234:{'amt':500,'name':'abc'}},
                        'user2':{134:{'amt':100,'name':'pqr'}}}
    def deposite(self,user,password,depo):
        self.details[user][password]['amt'] += depo
        a = self.details[user][password]['amt']
        print(f'the depo {depo} credited in your bank and total balance is {a}')
        
    def withdraw(self,user,password,withdraw):
        self.details[user][password]['amt'] -= withdraw
        a = self.details[user][password]['amt']
        print(f'the depo {withdraw} credited in your bank and total balance is {a}')
    def show(self):
        print(f'Total available balance is {self.amt}')
obj = Bank()
obj.deposite('user1',1234,30)
obj.withdraw('user1',1234,30)
