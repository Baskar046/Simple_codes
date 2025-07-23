input=int(input("enter the value:"))
total=0
total1=0
count=0
count1=0
for i in range(1,input+1):
    if i%2==0:
        print("even",i)
        count1=count1+1
        total += i
    else:
        print("odd",i)
        count=count+1
        total1+=total
print("no of even numbers:",count1,"total no of even:",total)
print("no of odd numbera:",count,"total no of odd numbers:",total1)