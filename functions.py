def sayHello(name = "sam"):
    print(f"Hello {name}")

def getSum(num1 = 1, num2 = 1, num3 = 1):
    return num1 + num2 + num3

sayHello()
print(getSum())

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similiar
# JS arrow functions.

lambSum = lambda num1, num2: num1 * num2
lambPrint = lambda : "Farhan Fatur"
print(lambSum(3, 20))
print(lambPrint())