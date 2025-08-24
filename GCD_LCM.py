#GCD
a=int(input("enter the a value :"))
b=int(input("enter the b value :"))
small=min(a,b)
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        gcd=i
print("gcd of and b is",gcd)


