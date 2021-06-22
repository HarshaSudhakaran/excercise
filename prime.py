n=int(input("enter a number"))
flag=False
if n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
        if flag:
            print(n,"not a prime")
        else:
            print(n,"a prime")
            
lower=int(input("enter lower range"))
upper=int(input("enter upper range"))

for num in range(lower,upper+1):
                  if num>1:
                      for i in range(2,num):
                          if (num%i)==0:
                              break
                          else:
                                print(num)
