# Variable Naming Convention
# start with letter or underscore
# can contain only alpha-numeric characters and underscore
# reserved keywords can not be used as variable name
# variable names are case sensitive

name='davood'
age=31
marks=90.8
isActive=True

print(name)
print(age)
print(marks)
print(isActive)

print(type(name))
print(type(age))
print(type(marks))
print(type(isActive))

#Casting variables

print('---------------------------------------------')
newMarks=str(97.8)
print(newMarks)
print(type(newMarks))


#Multiple Assignments in Single statement
print('------------------------------------')
a=b=c=10 # In case of same value
print(a,b,c)
a,b,c = 10,20,30 # In case of different value
print(a,b,c)

# Local Variables
# Variables defined within a function. We can not access these variables outside the function

# Global Variables
# Any variable created outside any function can be accessed within any function

# CONSTANTS
# Python has no formally defined Constants
# However, we can have a variable treated as Constant by using all caps names with underscore
# Example : PI_VALUE
