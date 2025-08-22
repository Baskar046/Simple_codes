#simple method
rev=int(str(n)[::-1])
print(rev)

#using while loop
n=int(input("enter the number:"))
count=1
while 0<n:
    count*=n%10
    n=n//10
print(count)

#using for loop
n=int(input())
count=0
for i in range(n+1):
    if n>0:
        count = (count * 10) + n % 10
        n = n // 10
print(count)

#using function
def rev(n):
    count=0
    while n>0:
        count=(count*10)+n%10
        n=n//10
    print(count)
rev(123)

#using class
class rev_num:
     def rev_function(self,num):
        count=0
        while num>0:
            count=(count*10)+num%10
            num=num//10
        print(count)
obj=rev_num()
obj.rev_function(1234)
