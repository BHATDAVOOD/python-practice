is_old = False
if is_old:
    print('You are old enough to drive')
else:
    print('You are not old enough to block')
print('This is out of if block')

# Ternary Operator / Conditional Expression

is_friend = True
can_message = "message allowed" if is_friend else "not allowed"
print(can_message)

# Short Circuiting
# This is a concept where only 1 condition is checked in case of and/or operators in case of miss or hit

has_book = True
has_vacancy = True

# This will check both and if first is false, it will short circuit and not check the next then
if has_book and has_vacancy:
    'You have both'

# If the first one is true, it will not care about the second one and short ciruit it    
if has_book or has_vacancy:
    'You have either one or both'