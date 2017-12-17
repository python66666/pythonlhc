import json
mm=[]
seven=[]
tm=[]
qs=[]
s12=[]
qs1=[]
with open ('C:/Users/WINkey/Desktop/LHC-PYTHON/lhc.json','r') as f:
    data = json.load(f)
    #print(data)


    for i in data:
        ss = i['xiaoma']+i['tm']
        seven.append(ss)
        for a in (i['qisu']):
            qs.append(a)


        
        #sixma.append(i['xiaoma'])
        #qs.append(i['qisu'])
        #tm.append(i['tm'])
           

        #print(i['xiaoma'])
    #print(data['xiaoma'])
#print(sixma)

#print(tm)
            
#print(seven_12)        


for i in qs:
    aa=int(i)
    qs1.append(aa)


#print(seven[0])

del seven[0]

tmd=dict(zip(qs1,seven))

#print(tmd)



file = open('lhc2.json','w',encoding='utf-8')
data = tmd
json.dump(data,file,ensure_ascii=False)
file.close()


