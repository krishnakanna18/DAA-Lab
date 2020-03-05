n=int(input("Enter the power"))
s=""
m=n
while(m>0):
  rem=m%2
  s=s+str(rem)
  m=m//2
#s=s[::-1]
print(s)
#mat=[[1,1],[1,0]]
fin=open('input.txt','r') #reads input from a file 'input.txt'
if(n==0):
  print([[1,0],[0,1]])
  print("The fibonacci term is",0)
  exit
mat=[]
for line in fin.readlines():
  mat.append([int(x) for x in line.split(',')])

term=mat
if(s[0]=='1'):
  result=mat
else:
  result=[[1,0],[0,1]]
def multiply(a,b):
   res=[[0 for i in range(len(a))] for j in range(len(b[0]))]
   #res=[[0,0],[0,0]] 
   for i in range(len(a)):
      for j in range(len(b[0])):
         res[i][j]=0
         for k in range(len(a[0])):
            res[i][j]+=a[i][k]*b[k][j]  
   return res   
for bit in s[1:len(s)]:
  term=multiply(term,term)
  if(bit=='1'):
    result=multiply(result,term)
print("The result of the exponentiation is->")
for oned in result:
    print(oned)
print("The",n,"th fibonnaci number is",result[0][1])

   
   

  

