# Lists are like Arrays in Java
li = [1,2,3,4]
li2= ['a','b','c']
li3 = [1,2,3,'a','b',True]

amazon_cart =[
    'notebooks',
    'books',
    'mobiles'
]

print(amazon_cart)

new_cart = amazon_cart
new_cart[0] = 'ipads'

print(new_cart)
print(amazon_cart) # Here amazon_cart is also changed as we are not copying the amazon_cart to new_cart. So now when we modify new_cart, we actually modify amazon_cart also. This can be handled as below

another_cart = new_cart[:] # Here we only copy the list and then modifying another_cart will not modify new_cart

another_cart[0] = 'furniture'
print(another_cart)
print(new_cart)

# List Unpacking
# We can assign variables to each element of list and if we want to assign variables to only few, we can then do so by adding a * and variable name to rest

basket = ['notebooks','books','cars','groceries','furniture']
print(basket)

notebooks, books, cars, *new_basket = ['notebooks','books','cars','groceries','furniture']
print(notebooks)
print(books)
print(cars)
print(new_basket)
