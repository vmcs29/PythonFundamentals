class MyClass:
    name = "Victor"

    """Inbuilt function for every class in Python"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a+b)


x = MyClass("john", 50)
print (x.name)
x.sum(4, 5)
print (x.age)
