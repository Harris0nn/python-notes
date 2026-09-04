
"""
Python Data Types:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# I will put every datatype in it's own function like a little room for each of them
# print() is to create space between every output to make it easier to read 


def DataType1():
    x = "Hello world!!"
    print(x, "data type is", type(x))
DataType1()
print()
def DataType2():
    x = 5
    print(x, "data type is", type(x))
DataType2()
print()
def DataType3():
    x = 5.5
    print(x, "data type is", type(x))
DataType3()
print()
def DataType4():
    x = 1j
    print(x, "data type is", type(x))
DataType4()
print()
def DataType5():
    x = ["corn", "beef", "tallow"]
    print(x, "data type is", type(x))
DataType5()
print()
def DataType6():
    x = ("oranges", "chocolate", "candy")
    print(x, "data type is", type(x))
DataType6()
print()
def DataType7():
    x =range(6)
    print(x, "data type is", type(x))
DataType7()
print()
def DataType8():
    x = {"name" : "John", "age" : 36}
    print(x, "data type is", type(x))
DataType8()
print()
def DataType9():
    x = {"apple", "banana", "cherry"}
    print(x, "data type is", type(x))
DataType9()
print()
def DataType10():
    x = frozenset({"berries", "pear", "cherry"})
    print(x, "data type is", type(x))
DataType10()
print()
def DataType11():
    x = True
    print(x, "data type is", type(x))
DataType11()
print()
def DataType12():
    x = b"Hello"
    print(x, "data type is", type(x))
DataType12()
print()
def DataType13():
    x = bytearray(3)
    print(x, "data type is", type(x))
DataType13()
print()
def DataType14():
    x = memoryview(bytes(7))
    print(x, "data type is", type(x))
DataType14()
print()
def DataType15():
    x = None
    print(x, "data type is", type(x))
DataType15()
print()

# Python Data types :D