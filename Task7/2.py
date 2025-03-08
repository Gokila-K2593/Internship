class BankAccount:
    def __init__(self,initial_balance=0):
        self.balance=initial_balance  
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print("Successfully deposited",amount)
        else:
            print("Deposit amount must be greater than zero.")
    def withdraw(self,amount):
        try:
            if amount>self.balance:
                raise ValueError("Insufficient funds. Withdrawal denied.")
            elif amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            else:
                self.balance-=amount
                print("Successfully withdrew",amount)
        except ValueError as e:
            print(e) 
    def check_balance(self):
        print("Current balance:",self.balance)
def main():
    print("Welcome to the Bank Account Simulator!")
    initial_balance=float(input("Enter initial deposit amount: "))
    account=BankAccount(initial_balance)  
    while True:
        print("\nOptions:\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Exit")
        choice=input("Enter your choice (1-4): ")
        if choice=="1":
            amount=float(input("Enter deposit amount: "))
            account.deposit(amount)  
        elif choice=="2":
            amount=float(input("Enter withdrawal amount: "))
            account.withdraw(amount)  
        elif choice=="3":
            account.check_balance()
        elif choice=="4":
            print("Thank you for using.")
            break 
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__=="__main__":
    main()