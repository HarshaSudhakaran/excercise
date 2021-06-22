s=input("enter string")
count=0
vowels=set("aeiou")
for i in s:
    if i in vowels:
        count=count+1
print("count of the vowels is:",count)
