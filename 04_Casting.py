"""
Casting in python is when you specify a type on a variable, it is done using constructor functions:

int - Constructs a integer number from a int literal, foat literal(removes all decimals) or a str literal(has to represent a float or integer)
float - Constructs a float number from a int literal, float literal or a string literal(has to represent a float or integer)
str - Constructs a string number from a int literal, float literal and string itself.

str = string
int = integer

"""

def intFunc():
    x = int(7) # This will stay as 7
    y = int(2.4) # This will be 2
    z = int("3") # This will stay as 3

    print(x) 
    print(y)
    print(z)

intFunc()
print()

def floatFunc():
    x = float(1) # This will be 1.0
    y = float(2.8) # This will stay as 2.8
    z = float("3") # This will be 3.0
    a = float("4.4") # This will stay as 4.2

    print(x)
    print(y)
    print(z)
    print(a)

floatFunc()
print()

def stringFunc():
    x = str("s1") 
    y = str(2)
    z = str(3.0)

    print(x)
    print(y)
    print(z)

stringFunc()