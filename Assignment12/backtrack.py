import math
from itertools import permutations

#Function to determine if a state is a goal state
def goal_state(s,g):
	for ind in range(len(s)-1):
		#visit[s[ind]]=1
		if s[ind+1] not in g[s[ind]]:
			return 0
	if s[len(s)-1] not in g[s[0]]:
		return 0
	return 1

#Function for printing the cycles
def map(gmap,res):
	print(res,end=': ')
	c=0
	d=dict((value,key) for key,value in gmap.items())
	for i in res:
		print(d[i],end='->')
	print(d[res[0]])

def check(visit):
	if(0 in visit):
		return 0
	return 1

# Find circuits using backtracking
def bt_ham(g,src,visit,res):
	visit[src]=1
	res.append(src)
	for v in g[src]:
		if(visit[v]!=1):
			bt_ham(g,v,visit,res)
	# print(res)
	if(check(visit)==0):
		visit[src]=0
		res.pop()
				
n=int(input())
g=[[]*n]*n
v=[]
gmap=dict()
vc=0
with open("n.txt") as f:
	for line in f:
		v1=line[0]
		v2=line[2]
		# print(v1,v2)
		if(v1 not in gmap):
			gmap[v1]=vc
			v.append(vc)
			g[gmap[v1]]=list()
			vc+=1
		if(v2 not in gmap):
			gmap[v2]=vc
			v.append(vc)
			g[gmap[v2]]=list()
			vc+=1
		# print(gmap)
		a=gmap[v1]
		b=gmap[v2]
		if(b not in g[a]):
			g[a].append(b)
		if(a not in g[b]):		
			g[b].append(a)
# print("The graph is :" ,g)
visit=[0]*n
res=list()
bt_ham(g,0,visit,res)
print()
print("Hamiltonian circuits using backtracking:")
map(gmap,res)
print()