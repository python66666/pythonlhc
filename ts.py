aa = [['11', '19', '49', '20', '02', '33', '06'],['07', '24', '26', '45', '39', '18', '44']
,['02', '31', '27', '33', '19', '10', '16'],['25', '22', '36', '01', '30', '13', '04']]
bb=[]
cc =[]


for i in aa:
    bb=[int(b)%12==0 and 12 or int(b)%12  for b in i]

    #print(bb)
    cc.append(bb)
print(cc)

'''
for i in aa:
    print(i)
    for b in i:
        b = int(b)%12
        if b == 0:
            b=12
        
        bb.append(b)       
    cc.append(bb)
    bb =[]
print(cc)
'''
