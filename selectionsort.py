def print_array(arr,low,high):
	sub=[]
	for num in range(low,high+1):
		sub.append(arr[num])
	print(sub)	 	
def read_array(arr):
	arr=[int(i) for i in input().split()] #Reads a single line input as an array
	return (arr,len(arr))
def minfind(arr,lo,hi):
		if(lo==hi):
			return (arr[lo],lo)
		else:
			mid=lo+(hi-lo)//2
			(min1,pos1)=minfind(arr,lo,mid)
			(min2,pos2)=minfind(arr,mid+1,hi)
			if(min1<=min2):
				return (min1,pos1)
			else:
				return (min2,pos2)
def minimum(arr):
	return minfind(arr,0,len(arr)-1)
def selsort(arr):
	for i in range(len(arr)-1):
		(min,pos)=minfind(arr,i,len(arr)-1)
		arr[pos],arr[i]=arr[i],arr[pos]
def main():
	arr=[]
	(arr,n)=read_array(arr)
	print("The read array->")
	print_array(arr,0,n-1)
	print("The minimum element is",minimum(arr)[0])
	selsort(arr)
	print("The sorted array is->")
	print(arr)
if __name__=='__main__':
	main()









