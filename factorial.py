n=int(input("enter the number:"))
count=1
if n==1:
    print("1")
elif n<=0:
    print("enter the valid number")
else:
    for i in range(1,n+1):
        count*=i
    print(count)

#find the factorial number using recursion function
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    ans = factorial(5)
    print(ans)

#finding factorial number using import method
import math         #default module
print(math.factorial(5))
