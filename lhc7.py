import pickle
import random

pickle_file = open('tmd.pkl','rb')
tmd = pickle.load(pickle_file)




class Fish:
    def __init__(self):
        self.x = random.randint(0,1)
        self.y = random.randint(0,10)

    def move(self):
        self.x -= 1
        print('我的作标为%s',self.x,self.y)

class goldfish(Fish):
    pass



class Numx:
    def __init__(self,q):
        q = str(q)
        self.a = tmd[q][0]
        self.b = tmd[q][1]
        self.c = tmd[q][2]
        self.d = tmd[q][3]
        self.e = tmd[q][4]
        self.f = tmd[q][5]
        self.g = tmd[q][6]






class Numa(Numx):
    pass
