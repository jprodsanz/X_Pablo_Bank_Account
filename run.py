class ChaseBank:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        ChaseBank.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self 

    def withdraw(self, amount):
        if(self.balance - amount) >= 0: 
            self.balance -= amount
        else:
            print('Not enough money: $5 overdraft fee will be assessed')
            self.balance -= 5
        return self 

    def account_info(self):
        print(f"Balance: {self.balance}")
        return self 

    def yield_int(self):
        if self.balance > 0: 
            self.balance += (self.balance * self.int_rate)
        return self 
    
savings = ChaseBank(.010,1500)
checking = ChaseBank(.05, 3500)

savings.deposit(5).deposit(10).deposit(45).withdraw(100).yield_int().account_info()
checking.deposit(10).deposit(15).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_int().account_info()