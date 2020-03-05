import time
#Functions from ques 3.................................
def ordered_insert_helper(num,arr,lo,hi,new): #Helper function of ordered insert
	if(lo==hi and arr[lo]>=num):
		new[lo+1]=arr[lo]
		new[lo]=num
		return lo
	elif(lo==hi):
		new[lo]=arr[lo]
		new[lo+1]=num
		return len(arr)
	mid=lo+(hi-lo)//2
	if(arr[mid]>=num):
		new[mid+2:hi+2]=arr[mid+1:hi+1]
		#print(new)
		hi=mid
	else:
		new[lo:mid+1]=arr[lo:mid+1]
		lo=mid+1
	return ordered_insert_helper(num,arr,lo,hi,new)
def ordered_insert(num,arr):
	new=[0 for i in range(0,len(arr)+1)]
	if(len(arr)==0):
		new[0]=num
	else:
		pos=ordered_insert_helper(num,arr,0,len(arr)-1,new)
	return new	
#1 recursive_ordered_merge.............
def ordered_merge(sub,arr):
	if(len(sub)==0):
		return arr
	else:
		return ordered_merge(sub[1:len(sub)],ordered_insert(sub[0],arr))
#2 iterative ordered_merge..............
def itr_ordered_merge(sub,arr):	
	for i in range(len(sub)):
		arr=ordered_insert(sub[i],arr)
	return arr
arr=[]
sub=[]
print("Enter the array")
start=time.time()
sub=[int(i) for i in input().split()]
# print("The sorted array is",ordered_merge(sub,arr))
# print("The time taken to sort is" ,(time.time()-start))
start2=time.time()
print("The sorted array is",itr_ordered_merge(sub,arr))
print("The time taken to sort is",(time.time()-start()))