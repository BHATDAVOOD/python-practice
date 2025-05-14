#Python Arithmetic Operators
# Used to perform basic arithmetic operations like Addition, Subtraction, DIvision, Multiplication etc

a,b,c=10,20,30

d=a+b+c
print("a : {} b : {} c : {} a+b+c : {}".format(a,b,c,d))

d=a+c-b
print("a : {} b : {} c : {} a+c-b : {}".format(a,b,c,d))

d=a*b
print("a : {} b : {} a*b : {}".format(a,b,d))

d=a/b
print("a : {} b : {}  a/b : {}".format(a,b,d))

e=21
d=e%a
print("a : {} e : {}  e%a : {}".format(a,e,d))

#Exponent (Power)
a,b=2,3
c=a**b
print("a : {} b : {}  a**b : {}".format(a,b,c))

#Floor Division : Returns only the integer part discarding the decimal part
c=9//4
print(c)

# Python comparision operators
# Compare values on each side of the operator and decide the relation
print("Python Comparision operators")
a=b=10
c=a==b
print(c)
print("a!=b : {}".format(a!=b))
print('a<b : {}'.format(a<b))
print('a>b : {}'.format(a>b))
print('a<=b : {}'.format(a<=b))
print('a>=b : {}'.format(a>=b))