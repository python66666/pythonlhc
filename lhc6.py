import pickle
import random

pickle_file = open('tmd.pkl','rb')
tmd = pickle.load(pickle_file)

def num12(a):
    a = a%12
    if a %12 ==0:
        a = 12
    return a


def gs1(a,b,):
    c = a - b
    global count
    c=abs(c)
    if c >5:
        c = c-5
    #print(c,'|',end='')
    if c <=5:
        print('1',end='')
        count+=1
    else:
        print('0',end='')
        
 #位置宽度   
    
def gs3(a,b,c):
    global count
    if a + 6 ==b or (a+6)%12==b or c+6 ==b or (c+6)%12 ==b:
        print('1',end='')
        count+=1
    else:
        print('0',end='')

def gs2(a,b,c):
    global count
    i = 6
    p = 6
    if a + i ==b or (a+i)%12==b or  c+6 ==b or (c+6)%12 ==b or a ==b:# or a + 6 ==b or (a+6)%12==b :
        if c == a:
            print("=",a,"=",end='')
        print('1',end='')
        count+=1
    else:
        print('0',end='')

def gs4(a,b):
    global count
    if a + 0 ==b or (a+0)%12==b:
        print('1',end='')
        count+=1
    else:
        print('0',end='')

def num9(a,b):
    co = 0
    global count
    for i in range(5,8):
        if a+i==b or (a+i)%12 ==b or (b ==12 and(a+i)%12 ==0):
            co=+1
    if co ==0:
        print('1',end="")
    else:
        count +=1
        print('0',end="")

def numxx(a,b,c,d):
    global count
    if a + 3 ==b or c ==b or d+6==b:# 
        print('1')
        count+=1
    else:
        print('0',end='')
        
def gs6(a,b):
    global count
    if a + 6 ==b or (a+6)%12==b:
        print('1',end='')
        count+=1
    else:
        print('0',end='')    
def gs7(b):
    global count
    i = random.randint(1,1000)
    if i ==b or (i)%12==b or (i%12==0 and b==12):
        print('1',end='')
        count+=1
    else:
        print('0',end='') 
count =0

for n in range(7):
    for q in tmd.keys():
        g1 = int(q)+1
        g = str(g1)
        
        if g1 <145:
            tm = tmd[g][6]
            b = int(tm)
            pm = tmd[q][n]
            pm1 = tmd[q][3]
            c = int(pm1)
            a = int(pm)
            #num9(a,b)
            gs7(b)
    print('-',n,'-->',count,'==',(143-count)/143)
    count =0

'''
for q in tmd.keys():
    g1 = int(q)+1
    g = str(g1)       
    if 20<g1 <70:
        tm = tmd[g][6]
        b = int(tm)
        pm = tmd[q][6]
        pm1 = tmd[q][2]
        pm2 = tmd[q][3]
        d = int(pm2)
        c = int(pm1)
        a = int(pm)
        #gs2(a,b,c)
        numxx(a,b,c,d)
print('-->',count,'==',(143-count)/143)
count =0
'''


