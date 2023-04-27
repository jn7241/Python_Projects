class bank_account:
    password = "1234"
    
    #constructor of the 2 attributes... Init automatically initializes the class
    def __init__(self, owner, info): 
        self.owner = owner #owner attribute
        self.info = info
        self.amount = 1500.0 #self.amount is balance attribute
        
    #login
    def login(self):
        if self.info == self.password:
            print("Signed in. Choose what you want to do...")
            return 2
        else:
            print("Incorrect password")
        return 0

    #balance
    def balance(self, count):
        try:
            if count == 0:
                self.account = self.amount
                count = 3
                
            if count == 1:
                self.account = self.account - self.draw
                count = 3
                
            if count == 2:
                self.account = self.account + self.add
                count = 3
                
            if count == 3:
                print(self.owner + ", your account has " + str(self.account) + " dollars.")
        except AttributeError as joe:
            self.account = self.amount
            count = 3
            print(self.owner + ", your account has " + str(self.account) + " dollars.")
        except ValueError:
            print("Invalid value...")
    #withdraw
    def withdraw(self, amount):
        try:
            if not(amount > self.account) and amount > 0:
                self.draw = amount
                self.balance(1)
            else:
                print("you can't do that (no amounts higher than in account)")
                self.draw = 0
        except AttributeError:
            self.account = 1500.0
            if not(amount > self.account) and amount > 0:
                self.draw = amount
                self.balance(1)
            else:
                print("you can't do that (no amounts higher than in account)")
                self.draw = 0
        except ValueError:
            print("Invalid value...")

    #deposit
    def deposit(self, amount):
        try:
            nothing = self.account - self.account # why not 0? I want to catch the error 'bank_account' object has no attribute named 'account'
            if amount > nothing:
                self.add = amount
                self.balance(2)
            else:
                 print("you can't do that (no amounts lower or equal 0)")
                 self.add = 0
        except AttributeError:
            if amount > 0:
                self.account = self.amount
                self.add = amount
                self.balance(2)
            else:
                print("you can't do that (no amounts lower or equal to 0)")
                self.add = 0
        except ValueError:
            print("Invalid value...")
        
  
            
        
            
name = input("Type your account name: ")
sign_in = 0
while sign_in != "-1" or a != 0:
    
    sign_in = input("type your password (-1 to exit): ")
    user = bank_account(name,sign_in)

    a=user.login()
    
    if a != 0:
        break
    
#i is an important "counter" to this program...
i = 0
while a !=0:
    try:
        z = input("Press 1 to withdraw, 2 to deposit, and 3 to check balance (-1 to logoff): ")
        
        if not(z== "1" or z == "2" or z== "3" or z== "-1"):
            print("You can only write values 1,2,3 and -1.")
            
        if z == "-1":
            print("logging off...")
            break
        if z == "1":
            i = 1
            user.withdraw(float(input("Type how much money you want to withdraw: ")))
            
        if z == "2":
            i = 2
            user.deposit(float(input("Type how much money you want to deposit: ")))
            
        if z == "3":
            i = 3 
            user.balance(i)
        
    except ValueError:
        print("Invalid value entered.")
        
    
    
