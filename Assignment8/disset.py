class set(object):
	__slots__=['parent','rank','size']
	def __init__(self,size):
		self.size=size
	def makeset(self):
		self.parent=[i for i in range(self.size)]
		self.rank=[0 for i in range(self.size)]
	def findset(self,u):
		if(self.parent[u]!=u):
			self.parent[u]=self.findset(self.parent[u])
		return self.parent[u]
	def link(self,u,v):
		if(self.rank[u]>self.rank[v]):
			self.parent[v]=u
		elif(self.rank[v]>self.rank[u]):
			self.parent[u]=v
		else:
			self.parent[v]=u
			self.rank[u]+=1	
	def union(self,u,v):
		print(self.parent)
		x=self.findset(u)
		y=self.findset(v)
		print(u,':',x,' ',v,':',y)
		self.link(x,y)


	


