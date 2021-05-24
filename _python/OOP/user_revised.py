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