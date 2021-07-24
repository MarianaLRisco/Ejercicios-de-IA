from queue import Queue
class zt:
    def __init__(self,x1,y1,x2,y2,ship,top):
        self.lm=x1
        self.lc=y1
        self.rm=x2
        self.rc=y2
        self.ship=ship
        self.top=top
temp = Queue(maxsize=0)
xx=[0,0,1,1,2]
yy=[1,2,0,1,0]
list=[]#Objectlist
index=0#Object pointer
def Isdangerous(temp):
    if (( temp.lm >= temp.lc and temp.rm >= temp.rc and temp.lm >= 0 and temp.lc >= 0 and  temp.rm >= 0 and  temp.rc >= 0)
            or (temp.lm >= 0 and  temp.lc >= 0 and  temp.rm >= 0 and  temp.rc >= 0 and  temp.lm == 0 and  temp.rm >= temp.rc)
            or (temp.lm >= 0 and  temp.lc >= 0 and  temp.rm >= 0 and  temp.rc >= 0 and temp.lm >= temp.lc and temp.rm == 0)):
        return 1
    else:
        return 0
def pd(p,index):
    for i in range(0,index):
        if(list[i].lm==p.lm and list[i].lc==p.lc and list[i].rm==p.rm and list[i].rc==p.rc and list[i].ship==p.ship):
            return 0
    return 1
def fin(temp):
    if temp.lm==0 and temp.lc==0 and temp.rm==3 and temp.rc==3:
        return 1
    return 0
def bfs():
    global index
    while temp.empty()==0:
        temp1=temp.get()
        x1=temp1.lm
        y1=temp1.lc
        x2=temp1.rm
        y2=temp1.rc
        for i in range(0,5):
            x=xx[i]
            y=yy[i]
            if temp1.ship==1:
                temp2=zt(x1-x,y1-y,x2+x,y2+y,-1,temp1.top+1)
                if fin(temp2)==1:
                    return
                if Isdangerous(temp2)==1 and pd(temp2,index)==1:
                    temp.put(temp2)
                    list.append(temp2)
                    index+=1
            else :
                temp2 = zt(x1 + x, y1 + y, x2 - x, y2 - y, 1, temp1.top + 1)
                if Isdangerous(temp2) == 1 and pd(temp2, index) == 1:
                    temp.put(temp2)
                    list.append(temp2)
                    index += 1


start=zt(3,3,0,0,1,0)
temp.put(start)
list.append(start)
index+=1
bfs()
print('Initial state',3,3,0,0)
for item in range(3,index-1):
    if list[item].ship==-1:
        if item==3:
            print(" A----->B:", end='')
        else:
             print("A----->B:",end='')
        print(list[item].lm,list[item].lc,list[item].rm,list[item].rc,'\n',end=' ')
    if list[item].ship==1:
        print("B----->A:",end='')
        print(list[item].lm,list[item].lc,list[item].rm,list[item].rc,'\n',end=' ')
print("Target Status:",0,0,3,3)
