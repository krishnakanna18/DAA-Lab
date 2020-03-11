import math
from itertools import permutations

def goal_state(s,g):
	for ind in range(len(s)-1):
		#visit[s[ind]]=1
		if s[ind+1] not in g[s[ind]]:
			return 0
	if s[len(s)-1] not in g[s[0]]:
		return 0
	return 1
		
def ham(n,g):
	for s in permutations(range(0,n)):
		if(goal_state(s,g)==1):
			#yield s
			print(s)

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
	print(res)
	if(check(visit)==0):
		visit[src]=0
		res.pop()
	# if(goal_state(res,g)==1):
	# 	return res
	# visit[src]=0
	# res.pop()
	# bt_ham(g,src,visit,res)
	

	
			
n=int(input())
g=[[]*n]*n
v=[]
vc=0
with open("hinp.txt") as f:
	for line in f:
		(a,b)=map(int,line.split(' '))
		if(a not in v):
			v.append(a)
			g[a]=list()
		if(b not in v):
			v.append(b)
			g[b]=list()
		#if(g[a] is None):
		#	g[a]=list()
		#if(g[b] is None):
		#	g[b]=list()
		if(b not in g[a]):
			g[a].append(b)
		if(a not in g[b]):		
			g[b].append(a)
print("The graph is :" ,g)
# print("Hamiltonian circuits using permutations:")
# ham(n,g)
visit=[0]*n
res=list()
bt_ham(g,0,visit,res)
print("Hamiltonian circuits using backtracking:")
print(res)
	