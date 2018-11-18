
# coding: utf-8

# In[155]:


import sys
import numpy as np
f = open(sys.argv[1],"r")
qstxt=open(sys.argv[3],"w")
vpol=open(sys.argv[4],"w")
vval=open(sys.argv[2],"w")
epoch=int(sys.argv[5])
gamma=float(sys.argv[6])
next ='a'
axel=0
nl=0
eps=0
cl=0
clmax=0
dirs=np.zeros((4))
op=-1
while next != (""):
    next = f.read(1)
    if next=="G" or next=="S" or next==".":
        axel=axel+1
    if(next=="\n"):
        nl=nl+1
        if(cl>clmax):
            clmax=cl
        cl=0
    else:
        cl=cl+1
f.close()
# print("number of elements in each row in maze: {}".format(clmax))
# print("number of lines in maze: {}".format(nl))
# print("number of non obstable elements: {}".format(axel))
vs=np.zeros((nl,clmax))
vsact=np.zeros((nl*clmax))
vs=np.matrix(vs)
maze1=np.chararray([nl,clmax])
vsdummy=vs
f = open(sys.argv[1],"r")
next=f.read(1)
j=0
k=0
while next != (""):
    if(next!="\n"):
        maze1[k,j]=next
        j=j+1
    if(next=="\n"):
        k=k+1
        j=0
    next=f.read(1)
qs=np.zeros((axel*4))
print(maze1)
for eps in range(epoch):
    for s in range(nl):
        for t in range(clmax):
            if(maze1[s,t]!="*"):
                if(t-1<0 or maze1[s,t-1]=="*"):
                    dirs[0]=-1.0+(gamma*vs[s,t])
                else:
                    dirs[0]=-1.0+(gamma*vs[s,t-1])
                if(t+1==clmax or maze1[s,t+1]=="*"):
                    dirs[2]=-1.0+(gamma*vs[s,t])
                else:
                    dirs[2]=-1.0+(gamma*vs[s,t+1])
                if(s-1<0 or maze1[s-1,t]=="*"):
                    dirs[1]=-1.0+(gamma*vs[s,t])
                else:
                    dirs[1]=-1.0+(gamma*vs[s-1,t])
                if(s+1==nl or maze1[s+1,t]=="*"):
                    dirs[3]=-1.0+(gamma*vs[s,t])
                else:
                    dirs[3]=-1.0+(gamma*vs[s+1,t])
                if(maze1[s,t]=="G"):
                    vsdummy[s,t]=0
                    vsact[op]=0
                else:
                    vsdummy[s,t]=np.max(dirs)  
                    vsact[op]=np.argmax(dirs)
                    
            elif(maze1[s,t]=="*"):
                vs[s,t]=999.0
                vsact[op]=6
            op=op+1
    vs=vsdummy
    op=0

for s in range(nl):
    for t in range(clmax):
        if(maze1[s,t]!="*"):
            if(t-1<0 or maze1[s,t-1]=="*"):
                dirs[0]=-1.0+(gamma*vs[s,t])
            else:
                dirs[0]=-1.0+(gamma*vs[s,t-1])
            if(t+1==clmax or maze1[s,t+1]=="*"):
                dirs[2]=-1.0+(gamma*vs[s,t])
            else:
                dirs[2]=-1.0+(gamma*vs[s,t+1])
            if(s-1<0 or maze1[s-1,t]=="*"):
                dirs[1]=-1.0+(gamma*vs[s,t])
            else:
                dirs[1]=-1.0+(gamma*vs[s-1,t])
            if(s+1==nl or maze1[s+1,t]=="*"):
                dirs[3]=-1.0+(gamma*vs[s,t])
            else:
                dirs[3]=-1.0+(gamma*vs[s+1,t])
            if(maze1[s,t]=="G"):
                qstxt.write("{} {} 0 {}\n".format(s,t,0.0))
                qstxt.write("{} {} 1 {}\n".format(s,t,0.0))
                qstxt.write("{} {} 2 {}\n".format(s,t,0.0))
                qstxt.write("{} {} 3 {}\n".format(s,t,0.0))
            else:
                qstxt.write("{} {} 0 {}\n".format(s,t,dirs[0]))
                qstxt.write("{} {} 1 {}\n".format(s,t,dirs[1]))
                qstxt.write("{} {} 2 {}\n".format(s,t,dirs[2]))
                qstxt.write("{} {} 3 {}\n".format(s,t,dirs[3]))
            vval.write("{} {} {}\n".format(s,t,vs[s,t]))
            vpol.write("{} {} {}\n".format(s,t,vsact[op]))
        op=op+1
            

qstxt.close()
vval.close()
vpol.close()

