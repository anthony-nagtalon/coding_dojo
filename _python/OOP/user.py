class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return False
            # Note: Balance can go under 0 if charged with less than $5 in account
        else:
            self.balance -= amount
            return True

    def display_account_info(self):
        return "Balance: ${}".format(self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (self.int_rate + 1)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate = 0.02, balance = 0)]

    def create_account(self, int_rate = 0.01, balance = 0):
        self.account.append(BankAccount(int_rate, balance))
        return self

    def verify_account_num(self, accIndex):
        if 0 <= accIndex < len(self.account):
            return True
        else:
            return False

    def make_deposit(self, amount, accIndex):
        if self.verify_account_num(accIndex):
            self.account[accIndex].deposit(amount)
            return True
        else:
            print("Invalid Deposit: User {} does not have an acct #{}.".format(self.name, accIndex))
            return False

    def make_withdrawal(self, amount, accIndex):
        if self.verify_account_num(accIndex):
            if self.account[accIndex].withdraw(amount):
                return True
        else:
            print("Invalid Withdrawal: User {} does not have an acct #{}.".format(self.name, accIndex))
        return False

    def display_user_balance(self):
        print("User: {}".format(self.name))
        for i in range(len(self.account)):
            print("[{}] {}".format(i+1, self.account[i].display_account_info()))

    def transfer_money(self, accIndex, recipient, recAccIndex, amount):
        # Check if acc numbers are valid for each user
        if self.verify_account_num(accIndex) and recipient.verify_account_num(recAccIndex):
            # Check if withdrawal is successful before depositing money to recipient
            if self.make_withdrawal(amount, accIndex):
                recipient.make_deposit(amount, recAccIndex)
        
        # Display which acc numbers are invalid
        else:
            if not self.verify_account_num(accIndex):
                print("Invalid Transaction: User {} does not have an acct #{}.".format(self.name, accIndex))
            if not recipient.verify_account_num(recAccIndex):
                print("Invalid Transaction: User {} does not have an acct #{}.".format(recipient.name, recAccIndex))
        return self

# Create 3 Instances of User
user1 = User("Catherine", "kyasurin@gmail.com")
user2 = User("Hye-lin", "exid_hyelin_seo@gmail.com")
user3 = User("Angie", "anjou_san@gmail.com")

# Return value changed from self to boolean for use in verifying transcations!
# Therefore, we cannot utilize chaining methods.
user1.create_account()
user1.make_deposit(100, 0)
user1.make_deposit(500, 1)
user1.display_user_balance()
print()

# We can still chain with create_account because it returns self
user2.create_account().create_account(0.15, 1000)
user2.make_deposit(250, 0)
user2.make_deposit(300, 1)
user2.display_user_balance()
print()

# Example of invalid deposit
user2.make_deposit(3, 3)
print()

# Example of invalid withdrawal
user3.make_withdrawal(1, 1)
print()

# Example of withdrawal with insufficient balance
user3.create_account(balance = 20).make_withdrawal(25, 1)
print()

# Example of successful transfer
user1.transfer_money(1, user3, 1, 200)
user1.display_user_balance()
user3.display_user_balance()
print()

# Example of invalid transfer indices
user1.transfer_money(2, user3, 2, 100)
print()

# Example of invalid transfer due to insufficient balance
user3.transfer_money(0, user2, 0, 10)
# Note: User3 will have a negative balance due to $5 fee
user2.display_user_balance()
user3.display_user_balance()