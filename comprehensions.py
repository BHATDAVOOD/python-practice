# This is an easier way to create List, Set and Dictonaries

# List Comprehension
# my_list = [param for param in Iterable ]

my_list = [char for char in 'hello']
print(my_list)

# we can use lambda functions and conditionals also in comprehensions
# Add Only even numbers to list from a range
my_list1 = [num for num in range(0,100) if num%2==0]
print(my_list1)

my_list2 = [num*2 for num in range(1,100)] # This is map function
print(my_list2)

# Dictionary Comprehensions
my_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

new_dict = {key:value**3 for key,value in my_dict.items() if value%2==0}
print(new_dict)