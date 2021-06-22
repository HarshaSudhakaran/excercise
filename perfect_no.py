#python pgm to check if a number is perfect or not
n=int(input('Enter a  Number'))
sum=0     
for i in range(1,n):
      if(n%i==0):
          sum=sum+i
if(sum==n):
      print('perfect Number')
else:
      print('Not Perfect Number')
      
