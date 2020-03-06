import math
from huffman import Node
class heaps(object):
	__slots__=['size','arr']
	def __init__(self,size,arr):
		self.size=size
		self.arr=arr
	def minheapify(self,i):
		l=2*i
		r=2*i+1
		if(l<self.size and self.arr[l].v<self.arr[i].v):
			mini=l
		else:
			mini=i
		if(r<self.size and self.arr[r].v<self.arr[mini].v):
			mini=r
		if(mini!=i):
			self.arr[i],self.arr[mini]=self.arr[mini],self.arr[i]
			self.minheapify(mini)
	def buildminheap(self):
		hs=self.size//2
		for i in range(hs,0,-1):
			self.minheapify(i)
		self.show()
	def maxheapify(self,i):
		l=2*i
		r=2*i+1
		if(l<self.size and self.arr[l]>self.arr[i]):
			maxi=l
		else:
			maxi=i
		if(r<self.size and self.arr[r]>self.arr[maxi]):
			maxi=r
		if(maxi!=i):
			#self.arr[i],self.arr[min]=self.arr[min],self.arr[i]
			temp=self.arr[i]
			self.arr[i]=self.arr[maxi]
			self.arr[maxi]=temp
			self.maxheapify(maxi)
	def buildmaxheap(self):
		hs=self.size//2
		for i in range(hs,0,-1):
			self.maxheapify(i)
		self.show()
	def ascheapsort(self):
		hs=self.size
		for i in range(hs-1,1,-1):
			self.arr[1],self.arr[i]=self.arr[i],self.arr[1]
			self.size-=1
			self.maxheapify(1)
		self.size=hs
		self.show()
	def descheapsort(self):
		hs=self.size
		for i in range(hs-1,1,-1):
			self.arr[1],self.arr[i]=self.arr[i],self.arr[1]
			self.size-=1
			self.minheapify(1)
		self.size=hs
		self.show()
	def extractmin(self):
		ret=self.arr[1]
		mini=self.arr[1]
		self.arr[1]=self.arr[self.size-1]
		self.arr.pop()
		self.size-=1
		self.minheapify(1)
		return ret
	def decreasekey(self,i,key):
		if(self.arr[i].v<key.v):
			print("Can't do....key less")
			return
		self.arr[i]=key
		parent=i//2
		while(i>1 and self.arr[parent].v>self.arr[i].v):
			self.arr[parent],self.arr[i]=self.arr[i],self.arr[parent]
			i=parent
			parent=parent//2
	def mininsert(self,key):
		self.size+=1
		new=self.arr+[0]
		self.arr=new
		self.arr[self.size-1]=Node(math.inf)
		self.decreasekey(self.size-1,key)
		self.show()
	def show(self):
		print()
		print("Resultant array: ",end=' ')
		for i in range(1,self.size):
			print(self.arr[i].ch,':',self.arr[i].v,end=' ')

