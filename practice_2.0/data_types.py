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