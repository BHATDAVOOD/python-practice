# Find duplicates

chars = ['a','b','c','d','b','d','e']

duplicates=[]
not_duplicates =[]
for character in chars:
    if character in not_duplicates:
        duplicates.append(character)
    else:
        not_duplicates.append(character)

print(duplicates)

# We can also do by checking if count is greater than 1, then add it to duplicates with another if check to confirm it is not already present in the duplicates list