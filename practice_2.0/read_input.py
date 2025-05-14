# Python provides built-in function to read input from the keyboard
# input() funtion
# It always reads data as string. We need to cast the data in case of different data type

print('Enter the name')
name=input()
#print('Hello : {}'.format(name))
city=input('Enter your city : ')
print('Hello {}, you are from {}'.format(name,city))

width=input('Enter width : ')
height=input('Enter height : ')
#area=width*height
#print('Area of rectangel is {}'.format(area))
#    area=width*height
#        ~~~~~^~~~~~~
#TypeError: can't multiply sequence by non-int of type 'str'

area=int(width)*int(height)
print('Area of rectangel is {}'.format(area))

