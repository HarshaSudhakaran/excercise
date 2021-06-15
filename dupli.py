p=[9,8,8,7,6,5,4,5,3,2,1]
q=set{}
uni=[]
for x in p:
    if x not in q:
        uni.append(x)
        q.add(x)
print(uni)
