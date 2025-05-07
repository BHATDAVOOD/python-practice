def say_hello():
    print("Hello!!!!")
    
say_hello()

# Parameters -> It is the values that a function will expect. Mentioned when we define the function
# Arguments -> It is the actual values that our function takes. Given at calling time

def say_something(name,email):
    print(f'Hello! Your name is {name} and email is {email}')


say_something('davood bhat','bhat@gmail.com')

# Positional Arguments -> In this type of arguments, we need to be pretty sure about the arguments. Suppose first parameter is name, so our first argument should be name only otherwise there could be discrepancies in our output

# Keyword Arguments -> In this type of arguments, we don't need to worry about the order of arguments as we will provide the keyword with arguments like name='davood',email='email@gmail.com'

say_something(email='email@gmail.com',name='abc')

# Default Parameters

def fun_with_default_parameters(name='default'):
    print(f'Your name is {name}')
    

fun_with_default_parameters('abcd')
fun_with_default_parameters() # Here we forgot to pass name, so defualt will be printed

# Docstring -> This is a way to inform what that function does

def fun_print(a):
    '''
    Info: This function tests and prints param a
    '''
    print(a)

fun_print('abc')

# *args and **kwargs
# *args defines that we can pass n number of arguments to a function. This will be stored as a tuple
# **kwargs defines that we can pass n number of keyword arguments to a function. This will be stored as a dictionary (Key:value pair)

def sum_numbers(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(sum_numbers(1,2,3,4,5,num1=10,num2=20,num3=30))

# Below rules must be taken care of:
# Parameter order is as : params, *args, default parameters, **kwargs

def difference_numbers(number1,*args,number2=3,**kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + number1 - number2 - total

print(difference_numbers(10,3,4,5,num1=3,num2=5))
    