class BankAccount:
    def __init__(self): 
        self.__balance = 0 
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited: {amount}.New balance:{self.__balance}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew:{amount}.New balance:{self.__balance}")
        elif amount>self.__balance:
            print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")
    def get_balance(self):
        return self.__balance
account = BankAccount()
account.deposit(1000)  
account.withdraw(500)
print("Final Balance:", account.get_balance())
