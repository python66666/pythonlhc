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
        print('0')
#9肖方式
def num91(a,b):
    count = 0
    for i in range(5,8):
        if a+i==b or (a+i)%12 ==b:
            count=+1
    if count ==0:
        print('1',end="")
    else:
        print('0')
#9肖方式
def num1(a,b):
    i = 1
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
def sin(a,b):
    if a in b:
        print('1',count,end='')
    
    #else:
        #print('0',end='')
#平特肖
def s1(a,b):
    i = random.randint(0,100)
    c = a+i
    if c %12 == 0:
        c = 12
        if c in b or c%12 in b:
            print('1')
        
"""
for i in tmd.items():
    print(i)

for n in range(7):
    for q in tmd.keys():
        g1 = int(q)+1
        g  = str(g1)
        if g1<145:
            b = tmd[g][6]
            a = tmd[q][n]
            num91(a,b)
    print('+++++',n,)
 """
#i = random.randint(0,100)
count =0
for n in range(7):
    for q in tmd.keys():
        g1 = int(q)+1
        g  = str(g1)
        if g1<145:
            a = tmd[q][n]
            c = tmd[q][6]
            b = tmd[g]
            a = (a+c)//2
            a = num12(a)
            if a in b:
                print('1',end='')
                count+=1
            else:
                print('0',end='')
    print('++++++',count,n)
    count =0

