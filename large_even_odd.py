a=[]
b=[]
c=[]
n=int(input("enter no of elements in list"))
for i in range(0,n):
   l=int(input("elements"))
   a.append(l)
for j in a:
   if(j%2==0):
      b.append(j)
   else:
      c.append(j)
print("large even",max(b))
print("large odd",max(c))
