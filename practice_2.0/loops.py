# 2 types of loops : for and while
# Control statements
# break : Terminates the loop execution and hands the control to the statement next to the loop
# continue : Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
# pass : The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

statement='''
hi this is a test case for loops.
let us try to implement loops.
'''

for char in statement:
    if(char not in 'aeiou'):
        print(char,end='')
        

numbers=(1,2,4,3,7,5,6)
total=0
for num in numbers:
    total+=num
print(total)

for num in range(5,15,2):
    print(num,end=' ')

print()
for num in range(5):
    print(num,end=' ')

print()
student={'name':'bhat','age':31,'marks':78.5}
for detail in student.items():
    print(detail)
