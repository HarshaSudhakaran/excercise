#python program to count the  number of digits in the number
n=int(input('Enter a Number'))
count=0
while(n>0):
    n=n//10
    count=count+1
print(count)
    
