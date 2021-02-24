import random 

list_of_acct_numbers = range(1, 10**8)   # [1: 9999999] 

random_number = random.randint(1, 10**8 - 1)  # # random 7 digit number => 0000006

class BankAccount():
      ROUTING_NUMBER = 12345678
      BALANCE = 0
      ACCOUNT_NUMBER = random.randint(1, 10**8 - 1)
     
def __init__(self, name, interest):
    self.name = name
    self.routing_number = BankAccount.ROUTING_NUMBER
    self.balance = BankAccount.BALANCE
    self.account_number = BankAccount.ACCOUNT_NUMBER
   
      
#deposit Method
def deposit(self, amount):
      amount = float(amount)
      self.balance = self.balance + amount

print(f"Amount You Have Just Deposited: $ " , self.amount)
print(f"Member Updated Balance: $ " , self.balance)

#withdraw Method
def withdraw(self,amount):
      #subtract amount from balance
      amount = float(amount)
      self.balance = self.balance - amount
      self.balance -= amount
      if self.balance >= 0:
        print(f"Amount You Have Withdrawn: $ " , self.amount)
        print(f"Member Updated Balance: $ " , self.balance)
       
       #overdaft Method
      else:
       # subtract ten dollar fee
       print("Insufficient funds available. You incurred a $10.00 overdraft fee. Why do you do this to yourself?")
       print(f"The current balance in your account is: $" , self.balance)


      #add_interest Method
def add_interest(self):
      interest = self.balance * .00083
      self.interest = interest
      self.balance = self.balance + interest

      #get_balance Method
def get_balance(self):
      print("Welcome to the Best Bank There Ever Was.")
      print(f"The current balance in your account is $" , self.balance)
      return self.balance


      #print_receipt Method
def print_receipt(self):
      self.rounded = str(round(self.balance, 2))
      print(" ")
      print("Account Summary:")
      print(" ")
      print(f"Name", self.name)
      print(f"Routing Number:", self.routing_number)
      print(f"Account Number:", self.random_number)
      print(f"Balance: $ " , self.rounded)

      #login_screen Method

def login_screen(account_list):
      print("Welcome to the Best Bank There Ever Was")
      name = input("Enter your name to log in or press 0 to exit:")
      if name == "0":
            return -1
      for i in range(len(account_list)):
            if name == account_list[i].name:
                return i
      return None

      #atm_menu created

def atm_menu():
        print(chr(27) + "[2J")
        print(" 1 for Deposit")
        print(" 2 for Withdrawal")
        print(" 3 for Receipt")
        print(" 0 for Log Out")
        print(" 4 for Exit")
        return (input("What would you like to do?: "))

#accounts created

BankAccount()  

if __name__ == "__main__":
        print(chr(27) + "[2J")
        account_list = []
        account_list.append(BankAccount("CaliR"))
        account_list.append(BankAccount("SuziI"))
        account_list.append(BankAccount("GabeJ"))
        account_list.append(BankAccount("TristanK"))
        account_list.append(BankAccount("CalebM"))
        account_list.append(BankAccount("LarissaN"))
        account_list.append(BankAccount("ZaidaM"))
        
        profile = None

while True:
            if not profile:
                #account_index
                profile = login_screen(account_list)
                if profile == None:
                    print("You are not a member of this bank. Please login with a member account.")
                if profile == -1:
                    break

if profile:
            selection = atm_menu()
            while 1:
              if selection == "1":
                  deposit_ammount = input("Enter ammount to deposit")
                  account_list[profile].deposit(deposit_ammount)
              elif selection == "0":
                    profile = None
              elif selection == "exit" or selection == "4":
               break
else:
                    print("System Does Not Recognise That Response. Please Enter Again.")

    


