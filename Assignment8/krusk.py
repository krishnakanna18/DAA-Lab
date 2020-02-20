from disset import *
from collections import defaultdict
class Edges(object):
	__slots__=['edges','size','vert']
	def __init__(self,edges,size,vert):
		self.edges=edges
		self.size=size
		self.vert=vert
	def sorti(self):
		for i in range(self.size):
			for j in range(i+1,self.size):
				if(self.edges[i][2]>self.edges[j][2]):
					self.edges[i],self.edges[j]=self.edges[j],self.edges[i]
	def kruskal(self):
		dset=set(self.vert)
		dset.makeset()
		A=list()
		self.sorti()
		for edge in self.edges:
			if(dset.findset(edge[0])!=dset.findset(edge[1])):
				A.append(edge)
				dset.union(edge[0],edge[1])
		print(A)
edges=list()
vert=list()
with open('inp.txt') as f:
	for line in f:
		edge=[int(v) for v in line.split(' ')]
		if(edge[0] not in vert):
			vert.append(edge[0])
		if(edge[1] not in vert):
			vert.append(edge[1])
		edges.append(edge)
graph=Edges(edges,len(edges),len(vert))
graph.kruskal()







