import json
import pickle 

s12=[]
s7=[]
qs=[]
tmd={}
with open('lhc2.json','r',encoding='utf-8')as f:
    data = json.load(f)
    for i in data.values():
        s7 = [int(b)%12==0 and 12 or int(b)%12  for b in i]
        s12.append(s7)
#print(s12) 余12后的值
    for q in data.keys():
        qs.append(q)
    #print(qs) 期数

tmd = dict((zip(qs,s12)))
#print(tmd) #总表
''' 
for i in tmd.values():
    print(i)
'''
#查询值
pickle_file = open('tmd.pkl','wb')
pickle.dump(tmd,pickle_file)
pickle_file.close()
