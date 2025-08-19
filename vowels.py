n=input("enter the word:")
count=0
a=['a','e','i','o','u']
for i in n:
    if i in a:
        count+=1
        print(i,end=" ")
print(count)
