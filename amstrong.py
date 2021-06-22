n=int(input("enter a no: "))
temp=n
sum=0
while(temp>0):
    i=temp%10
    sum=sum+pow(i,3)
    temp=temp//10
if(n==sum):
    print(n,"Amstrong Number")
else:
    print(n," Not Amstrong Number")
