# Python Numeric Data Types
# int, bool, float, complex
# complex - made of 2 parts - real & imaginary separated by + or - sign. Imaginary is suffixed by 'j'

complexType=4+5j
print(complexType)
print(type(complexType))

a,b,c,d = 10,20.7,False,10+3j
print("The type of variable having value ",a," is ",type(a))
print("The type of variable having value ",b," is ",type(b))
print("The type of variable having value ",c," is ",type(c))
print("The type of variable having value ",d," is ",type(d))

# Python String Data Type
# Enclosed in Single,Double or Triple Quotation marks
print('=======================================')

firstName='davood'
middleName="ahmad"
lastName='''bhat'''

print(firstName,middleName,lastName)
print(type(firstName),type(middleName),type(lastName))

# Arithmetic operations can not be performed on String Data type
# But Slicing and Concatenation can be performed

print(firstName[0]) # Prints first character
print(firstName[2:4]) # Prints from 2nd Index till 3rd Index 
print(firstName[2:]) # 2nd Index till end
print(firstName[:3]) # Starting to 2nd Index


# Python Sequence Data Types
# List, Tuple, Range
# List -> Data separated by commas and contained within square braces.
# Python Lists can have data of different types
# List can have simple number, string, tuple, dictionary,set or object of user defined class

print('=======================================')
data=[2025,"UST",22.6,True,6+3j]
print(data)
print(type(data))

# Tuple Data Type : Similar to List but is immutable

print('=======================================')

newData=(1,2,2.0,'Global',True)
print(newData)
print(type(newData))

# Python Range Data Type
# Represented by Range Class
# range(start,stop,step)  -> start : From where to Start, (Optional and Default is 0). Stop : Where to Stop, (Mandatory). Step : How to increment, (Optional and Default : 1)
# Range is used to iterate over a range of items

print("==================================")
for i in range(5):
    print(i)


# Python Binary Data Types -> 0 and 1
# Types : bytes, bytearray, memoryview

# byte data type : Sequence of bytes. Each byte is an integer value from 0 to 255.
# Commonly used to store binary data like images, files or network packets
# bytes() function is used to create bytes

print("==================================")
b1=bytes([67,68,69,70])
print(b1)

# bytearray data type : Similar to bytes but this is mutable. Data can be modified once created
# bytearray() function is used to create bytearray

value=bytearray([67,101,108,69])
print(value)

# memoryview data type : provides view into memory of original data. Access underlying data without copying it, providing efficient memory access.
# memoryview() construcors, slicing bytes or bytearray, extracting from array objects or open() function are ways to create memoryview

latestData=bytearray(b'Hello, world!')
view=memoryview(latestData)
print(view)