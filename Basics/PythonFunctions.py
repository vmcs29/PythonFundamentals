# Basic Syntax for functions in Python
# def func_name(parameter):
#     body

def printHello():
    print("Hello")


printHello()


def printHi(name="John"):
    print("Hi , " + name)


printHi("Victor")
printHi()


def sumFuction(a, b, c):
    print(a+b+c)


sumFuction(10, 15, 20)


def returnSum(a, b):
    """this is a function to calculate sum of 2 numbers"""
    return a + b


x = returnSum(10, 20)
print x

