# TASK 1. Create a class called BankAccount with the attributes: - account number , balance , owner name , date opened

class Bank_account:
   def __init__(self,account_no,owner_name,balance,date_opened):
    self.account_no=account_no
    self.owner_name= owner_name
    self.balance=balance
    self.date_opened=date_opened
    
    
# 2.Add some behaviour to the above class using the methods: - deposit() - withdraw() - check_balance() -display_info() -close_account()
   def deposit (self,amount):
        self.balance += amount
        print(f"You have successfully deposited ksh {amount}.") 
     
   def withdraw(self,amount):
      if amount <= self.balance:
         self.balance -= amount
         print(f"You have successfully withdrawn ksh {amount}.")  
      else:
         print("Insufficient funds")
    
   def check_balance(self):
       print(f"Your balance is currently ksh {self.balance}")

   def display_info(self):
      print(f"Account Number:{self.account_no} - Owner Name:{self.owner_name} -  Current Balance:ksh {self.balance} - Date Opened - {self.date_opened}")
      

   def close_account(self):
      print(f"Account {self.account_no} has been closed.")
      print("--------------------------------------------------------------")

account1=Bank_account("001","Mitchelle",50000)
account1.display_info()
account1.deposit(13000)
account1.withdraw(8000)
account1.check_balance()
account1.close_account()

# 3.Create two BankAccount objects that can deposit , withdraw , check balance display info and close account..

account2=Bank_account("002","James",70000)
account2.display_info()
account2.deposit(25000)
account2.withdraw(10000)
account2.check_balance()
account2.close_account()

account3=Bank_account("003","Alexia",150000)
account3.display_info()
account3.deposit(46000)
account3.withdraw(15000)
account3.check_balance()
account3.close_account()
       



