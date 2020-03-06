import math
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
		# self.show()
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
		# self.show()
	def show(self):
		print()
		print("Resultant array: ",end=' ')
		for i in range(1,self.size):
			print(self.arr[i].ch,':',self.arr[i].v,end=' ')

class Node(object):
	def __init__(self,val,ch='-'):
		self.l=None
		self.r=None
		self.v=val
		self.ch=ch
	def __str__(self):
		return str(self.v)+':'+str(self.ch)
def rec(root,code):
	if(root.l==None and root.r==None):
		print(root.ch,':',code)
		return
	rec(root.l,code+'0')
	rec(root.r,code+'1')
def huffman(hheap):
	hheap.buildminheap()
	# hheap.show()
	while(hheap.size>2):
		obj1=hheap.extractmin()
		obj2=hheap.extractmin()
		# print(obj1.v,obj2.v)
		new=Node(obj1.v+obj2.v)
		new.l=obj1
		new.r=obj2
		hheap.mininsert(new)
	# hheap.show()
	print()
	rec(hheap.arr[1],'')
string=input()
d=dict()
for ele in string:
	if(ele not in d):
		d[ele]=1
	else:
		d[ele]+=1
# print(d)
arr=[-1]
c=1
for ele in d:
	arr.append(Node(d[ele],ele))
	c+=1
hheap=heaps(c,arr)
# print(hheap.arr)
print("The huffman code for the above word:",end=' ')
huffman(hheap)

