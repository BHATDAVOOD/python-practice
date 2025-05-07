print('Davood Bhat')
# designation = input('What is your Designation?\n')
# print('You are a '+designation)

# Fundamental Data Types
int
float
complex
bool
str
list
tuple
set
dict

# Classes -> Custom Types

# Specialized Data Types -> Not inbuilt in Python but we can use from external packages (Modules)

# None
None

# Variables
# Rules
# snake_case
# start with lowercase or underscore
# can contain numbers, letters and underscore
# case sensitive
# don't override keywords

# Constants
# Good Convention is to have Constants in UPPER CASE only
PI = 3.14
print(PI)

# Augumented Assignment Operator
sum = 5;
sum = sum + 2;
print(sum)

# Above statements can be written as below using Augumented Assignment Operator
sum1 = 5;
sum1 += 2;
print(sum1)

# Strings -> str
# Strings can be written in below three ways

first_name = 'davood'
middle_name = "ahmad"
introduction = '''
My name is Davood Bhat
I am a Software Developer
I work in UST GLobal
'''

print(first_name)
print(middle_name)
print(introduction)

# Escape Sequence
# \ -> This lets interpreter to know that anything after this is also a String
# \t -> Add Tab 
# \n -> Add new Line

# Formatted Strings
# This helps us in writing dynamic stuff in a better way

name = "Davood Bhat"
age = 31

print('Hi '+ name +'. You are '+str(age) +' years old.')

# We can convert this to below with formatted Strings. This is preffered

print(f'Hi {name}. You are {age} years old.')

# Another way to do so

print('Hi {}. You are {} years old'.format('Davood Bhat','31'))

work = 'UST Global'
print('Hi {}. You work at {}.'.format(name,work))

print('Hi {0}. You work at {2}. YOu are {1} years old.'.format(name,age,work))

# Character at any Index, Sub String, Length
name = "Davood Bhat"
# Length
print(len(name))
# Character at index
print(name[0])
#Sub String (String slicing)
print(name[0:6])
print(name[7:]) # start at index 7 till end
print(name[:6]) # start from begining at stop at index 6
print(name[:])

# Step over -> Default is 1 as we print 1 character after other but we can change it
print(name[0:11:2]) # Begining to End with a step over of 2

# How to print from back or reverse a string.
print(name[-1])
print(name[::-1]) # This will reverse the name