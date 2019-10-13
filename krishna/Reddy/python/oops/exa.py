class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def make_deposite(self,amount):
        self.balance+=amount
    def make_withdraw(self,amount1):
        if self.balance<amount1:
            print("Eroor:Not enough funds")
        else:
            print("Successfully withdrawn amount: $",amount1,sep="")
            self.balance-=amount1
    def get_balance(self):
        return self.balance

a=BankAccount(5000)
print("current balance: $",a.get_balance(),sep="")
print("withdrawn amount 10000..... ")
a.make_withdraw(10000)
print("lets try again withdrawn amount 2000..... ")
a.make_withdraw(2000)
print("corrent balance: $",a.get_balance(),sep="")
print("depodsite $3000")
a.make_deposite(3000)
print("now corrent balance: $",a.get_balance(),sep="")

