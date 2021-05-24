class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: {}, Balance: ${}".format(self.name, self.account_balance))

    def transfer_money(self, recipient, amount):
        self.account_balance -= amount
        recipient.account_balance += amount
        return self

# Create 3 Instances of User
user1 = User("Catherine", "kyasurin@gmail.com")
user2 = User("Hye-lin", "exid_hyelin_seo@gmail.com")
user3 = User("Angie", "anjou_san@gmail.com")

# Make 3 deposits, 1 withdrawal
user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(250).display_user_balance()

# Make 2 deposits, 2 withdrawals
user2.make_deposit(50).make_deposit(175).make_withdrawal(25).make_withdrawal(100).display_user_balance()

# Make 1 deposit, 3 withdrawals
user3.make_deposit(3000).make_withdrawal(250).make_withdrawal(200).make_withdrawal(150).display_user_balance()

# Tranfer money from the first user to third user
user1.transfer_money(user3, 100).display_user_balance()
user3.display_user_balance()

class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            # Note: Balance can go under 0 if charged with less than $5 in account
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: ${}".format(self.balance))

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (self.int_rate + 1)
        return self

acct1 = BankAccount()
acct2 = BankAccount()

acct1.deposit(500).deposit(50).deposit(5).withdraw(412).yield_interest().display_account_info()
acct2.deposit(1000).deposit(500).withdraw(25).withdraw(75).withdraw(550).withdraw(125).yield_interest().display_account_info()