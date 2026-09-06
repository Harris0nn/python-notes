""""
The numeric types in python are:
- int ( x = 1 )
- float ( y = 2.8 )
- complex ( z = 1j )
"""

# Each numeric type will have their own function so there is no confliction

def intFunc(): # An int or integer is a whole number, postive or negative but with no decimals and no maximum length
    x = 7
    y = 39293842948
    z = 7333733

    print("These are int numbers")
    print(x, "is", type(x))
    print(y, "is", type(y))
    print(z, "is", type(z))
intFunc()
print()

def floatFunc(): # A flot is a number, positive or negative that contains one or more decimals
    x = 7.33
    y = 3.0
    z = 78.99
    a = 39e7

    print(x, "is", type(x))
    print(y, "is", type(y))
    print(z, "is", type(z))
    print(a, "is", type(a))
floatFunc()
print()

def complexFunc(): # A complex number is written with a "j" as the imaginary part
    x = 3+7j
    y = 7j
    z = -7j

    print(x, "is", type(x))
    print(y, "is", type(y))
    print(z, "is", type(z))
complexFunc()
print()

def ConversionFunc(): # This shows that you can and how to convert the different number types 
    x = 7  
    y = 3.3
    z = 8j

    a = float(x) # This is a int that turns into a float

    b = int(y) # This is a float that turns into a integer

    c = complex(x) # This is a int that converts to a complex 
    # A complex number(s) cannot be converted

    print(x, "is now type", type(a))
    print(y, "is now type", type(b))
    print(z, "is now type", type(c))
ConversionFunc()
print()

def RandNum(): # This is using import so we can randomise the number that is printed
    import random 
    print(random.randrange(1, 30), "This is a random number between 1 and 30!")      
RandNum()

# Python numbers :D