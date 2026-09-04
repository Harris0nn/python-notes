# Variables (They are case sensitive)
Myvar = "Different variable with uppercase M"
myvar = "Word Variable"
print(myvar)
print(Myvar)


x = 5
p = 5
k = "- Should equal 10" # x(5) and p(5) should equal to ten(k)
z = float(7) # Turns the number into a decimal
print(x + p, k,)
print(z) # Prints 7.0

# gets the typpe of variable
m = 5
n = 5.0
c = "Harrison"

print(m, "is", type(m)) # Prints <class 'int'>
print(n, "is", type(n)) # Prints <class 'float'>
print(c, "is", type(c)) # Prints <class 'str'>

# collection of values
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Harrison" # This is a global variable
c = "Bingo" # This is another global variable 

def func1():
    #The global keyword will change the scope of the variable below
    #global x = "Harrison" 
    x = "Harry" #This is a local variable that can only be used within the function
    print("i am", x) #This will print Harry because it is using the variable within the function
    print(c) # This will use the global variable since there is no local variable using c

func1()

print("i am", x) #This will print Harrison since it is using the global variable

# Python variables :D