#Decision making statements
# if,elif,else

marks=90
if(marks>90):
    print('A+ Grade')
elif(marks>80 and marks <=90):
    print('A Grade')
elif(marks>60 and marks <=80):
    print('B Grade')
elif(marks>33 and marks<=60):
    print('C Grade')
else:
    print('Fail')
    
# Match Statement - Similar to switch statements

def checkVowel(a):
    match a:
        case 'a':return 'Vowel'
        case 'e':return 'Vowel'
        case 'i':return 'Vowel'
        case 'o':return 'Vowel'
        case 'u':return 'Vowel'
        case _:return 'Consonant'

print(checkVowel('a'))
print(checkVowel('e'))
print(checkVowel('b'))
