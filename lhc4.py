import pickle
import random

pickle_file = open('tmd.pkl','rb')
tmd = pickle.load(pickle_file)

def num12(a):
    a = a%12
    if a %12 ==0:
        a = 12
    return a
#求余方式
def num6(a,b):
    count = 0
    for i in range(4,9):
        if a+i==b or (a+i)%12 ==b:
            count=+1
    if count ==0:
        print('1',end="")
    else:
        print('错',end="")
#6肖方式
def num9(a,b):
    count = 0
    for i in range(5,8):
        if a+i==b or (a+i)%12 ==b:
            count=+1
    if count ==0:
        print('1',end="")
    else:
        print('错',end="")
#9肖方式
def num1(a,b):
    i = 6
    if a+i==b or (a+i)%12 ==b:
        #i+=1
        print('错',end='')
    else:
        print('1',end='')
#杀一肖方式
        
def num0(a,b):
    if a==b or a%12 ==b:
        print('错',end='')
    else:
        print('1',end='')
# 本号A=B的方式
def numx(a,b):
    i = random.randint(1,13)
    if a+i==b or (a+i)%12 ==b:
        print('错',end='')
    else:
        print('1',end='')
#随机值方式
"""        
for q in tmd.keys():
    qs = int(q)
    g  = str(qs+1)
    tm = tmd[q][6]
    b = int(tm)
    
    n=0
    while int(g) <145:
        z = tmd[g][n]
        a =int(z)
        num9(a,b)
"""    
for n in range(7):
    for q in tmd.keys():
        g1 = int(q)+1
        g = str(g1)
        x = int(tmd[q][6])
        if int(g)<145:
            tm = tmd[g][6]
            b = int(tm)
            z = tmd[q][n]
            a = int(z)
            
            a=num12(a) 
            num9(a,b)
            #print('--',q,'--',end='')
            
    print('++++',n,)
           

    
    
        

    
       

