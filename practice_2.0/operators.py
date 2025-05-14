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

#Python Assignment operators
print('================ASSIGNMENT OPERATORS=====================')
a=10 
a+=10 # a=a+10 : 20
print(a)
a-=5 # a=a-5 : 15
print(a)
a*=5 # a=a*5 : 75
print(a)
a/=5 # a=a/5 : 15.0
print(a)
a%=4 # a=a%5 : 3
print(int(a))
a**=4 # a=a**4 : 81
print(int(a))
a//=4 # a=a//3 : 20.0
print(int(a))


#Python BITWISE operators
# & : AND, | : OR,  ^ : XOR, ~ : COMPLEMENT, << : ZERO FILL LEFT SHIFT, >> : SIGNED RIGHT SHIFT 
print('================BITWISE OPERATORS=====================')
a,b=20,10
print('a= ',a,' : ',bin(a),' b= ',b,' : ',bin(b))
c=0
c=a&b
print('result of a AND b is ',c,' : ',bin(c))
c=a|b
print('result of a OR b is ',c,' : ',bin(c))
c=a^b
print('result of a XOR b is ',c,' : ',bin(c))
c =~a
print('result of c COMPLEMENT a is ',c,' : ',bin(c))
c=a<<2
print('result of LEFT SHIFT is ',c,' : ',bin(c))
c=a>>2
print('result of RIGHT SHIFT is ',c,' : ',bin(c))

#Python Logical Operators
# and : AND -> a and b, or : OR -> a or b, not : NOT -> not(a)

print('==============LOGICAL OPERATORS======================')
number=35
print(number > 20 and number < 45)
print(number > 35 or number < 40)
print(not(number > 20))