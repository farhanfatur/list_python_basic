class User:
    level = "admin"
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and i am {self.age}"

    def incrementAge(self):
        self.age += 1
    def userText(self):
        return "from class User"

# extend class
class customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance = 0):
        self.balance = balance

    # overwrite
    def greeting(self):
        return f"My name is {self.name} and i am {self.age}, my balance is {self.balance}"

    def customerText(self):
        return "from class Customer"

user = User("Farhan", "farhan@email.com", 19)
customers = customer("Yasa", "yasa@email.com", 15)

# print(user.customerText())

customers.set_balance(500)
print(customers.greeting())
customers.incrementAge()
print(user.greeting())
print("level :", user.level)
user.level  = "superadmin"
print("level :", user.level)