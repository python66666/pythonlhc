a = [1,2,3,4,5,6,7,8,9,10,11,12]

b = [12]
g = b[0]

for i in a:
    if (i+5)%12 ==g or (i+6)%12 ==g or (i+7)%12==g:
        print('0')
    if g ==12:
        print('0')
    else:
        print('1')
        
