picture = [
    [0,0,1,1,1,0,1],
    [1,0,0,0,1,0,1],
    [1,1,0,1,1,0,0],
    [0,1,0,0,1,0,1],
    [0,0,1,0,1,0,0],
    [1,1,1,1,0,0,0]
]

for image in picture:
    for pixel in image:
        if pixel == 1:
            print('*',end='') # by default end = '\n' which gives a new line but we don't need it
        else:
            print(' ', end='')
    print()
    

picture1 =[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in picture1:
    for column in row:
        if column == 1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')