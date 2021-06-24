#generate a python list of all even numbers between 4-30
a=[]
for x in range(4,30):
    if x%2==0:
        a.append(x)
print(a)
