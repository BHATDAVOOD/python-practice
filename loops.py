for item in [1,2,3,4,5]:
    print(item)
    

# Iterable -> Collection of Items - List/Dictionary/Tuple/Set/String which can be iterated upon

user = {
    'name':"Davood Bhat",
    'age': 31,
    'on_bench':True
}

for person in user.items():
    print(person)
    
for person in user.keys():
    print(person)
    
for person in user.values():
    print(person)
    
for key,value in user.items():
    print(key,value)
    

my_list = [1,2,3,4,5,6,7,8,9]
count = 0
sum = 0
for number in my_list:
    count +=1
    sum += number
print(count)
print(sum)


# enumerate -> Gives us both index and value

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i)