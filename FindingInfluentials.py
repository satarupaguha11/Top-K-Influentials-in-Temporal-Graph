from gmlConvert import txttogml
import sys
#takes input graph from text file
textInput=sys.argv[1]

#converting graph to gml format
g=txttogml(textInput)
influence=[]
k={}
nodes=[]

#Controlled Iterative Depth First Search
def idfs(g,start):
    stack=[start]
    k={}
    a=[]
    k.update({start:0})
    
    count=0
    while stack:
        v=stack.pop()
        count=count+1
        for i in g.neighbors(v):
            if((k.has_key(i)!=True) and (k[v]+1/g[v][i]['weight']<=1)): #we consider spread within 1 timestamp
                stack.append(i)
                k.update({i:(k[v]+1/g[v][i]['weight'])})
                if(a.count(i)==0):
                    a.append(i)  
    return count,a


#computing influence of all the nodes
for i in range(g.order()):
    count1,b=idfs(g,i+1)
    influence.append(count1)
    nodes.append(b)

#propagation of influence    
newCount=influence
max1=0;
pos=0;
grey=[];
black=[];
while(len(grey)!=g.order()):
    
    max1=0;
    for i in range(len(newCount)):
        if(newCount[i]>max1):
            max1=influence[i];
            pos=i;
    print("Black node entered "+str(pos+1))
    black.append(pos+1)
    if(grey.count(pos+1)==0):
        grey.append(pos+1)
    for a in nodes[pos]:
        if(grey.count(a)==0):
            grey.append(a);
    newCount=[]
    for a in range(len(nodes)):
        count1=0
        for b in nodes[a]:
            if(grey.count(b)==0):
                count1=count1+1
        newCount.append(count1)
    print("The nodes in grey")
    print(grey)
