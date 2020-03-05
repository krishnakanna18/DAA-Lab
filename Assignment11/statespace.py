import math
from collections import defaultdict

# function to check if the assignment is right
def check(s,s1,s2,s3,l):
	d=defaultdict()
	for (i,j) in zip(s,l):
		d[i]=j
	# print(d)
	num1=0
	dij=1
	for i in s1[::-1]:
		num1+=dij*d[i]
		dij*=10
	# print(num1)
	dij=1
	num2=0
	for i in s2[::-1]:
		num2+=dij*d[i]
		dij*=10
	# print(num2)
	dij=1
	num3=0
	for k in s3[::-1]:
		num3+=dij*d[k]
		dij*=10
	# print(num3)
	if(num1+num2==num3):
		ans=dict(d)
		print("The correct assignment is:",ans)
		print(s1,":",num1)
		print(s2,":",num2)
		print(s3,":",num3)
	return 1
s1,s2,s3=input().split(',')
s=[]
for i in s1+s2+s3:
	if(i not in s):
		s.append(i)
count=0
for a1 in range(0,10):
	emp=[]
	emp.append(a1)
	for a2 in range(0,10):
		if(a2 not in emp):
			emp.append(a2)
			for a3 in range(0,10):
				if(a3 not in emp):
					emp.append(a3)
					for a4 in range(0,10):
						if(a4 not in emp):
							emp.append(a4)
							for a5 in range(0,10):
								if(a5 not in emp):
									emp.append(a5)
									for a6 in range(0,10):
										if(a6 not in emp):
											emp.append(a6)
											for a7 in range(0,10):
												if(a7 not in emp):
													emp.append(a7)
													for a8 in range(0,10):
														if(a8 not in emp):
															emp.append(a8)
															for a9 in range(0,10):
																if(a9 not in emp):
																	emp.append(a9)
																	for a10 in range(0,10):
																		if(a10 not in emp):
																			emp.append(a10)
																			check(s,s1,s2,s3,emp)
																			count+=1
																			emp.pop()
																	emp.pop()
															emp.pop()
													emp.pop()
											emp.pop()
									emp.pop()
							emp.pop()
					emp.pop()
			emp.pop()
