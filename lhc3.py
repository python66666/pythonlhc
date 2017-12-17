import pickle

tm=[]
qs=[]

qstm={}
pickle_file = open('tmd.pkl','rb')
tmd = pickle.load(pickle_file)

#print(type(tmd))

for i in tmd.values():
    #print(i)
    a = i[6]
    tm.append(a)
#print(tm) 打印特码

for i in tmd.keys():
    qs.append(i)
#print(qs) 打印期数

#qstm=dict(zip(qs,tm))
#print(qstm)
#期数对应特码表

for q in tmd.keys():
   for n in range(7):
        a = tmd[q][n]
        g = str(int(q)+1)
        if int(g) <145:
            b = (tmd[g][6])
            A = int(a)*6
            B = int(b)
           # print(q,':',A,'---',g,':',B)

            if A+5 == B or A+6 == B or A+7 ==B or (A+5)%12 == B or (A+6)%12 == B or (A+7)%12 == B:
                print('错')
            else:
                print('中',end='')
        
      
      

