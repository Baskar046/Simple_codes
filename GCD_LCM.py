#GCD
a=int(input("enter the a value :"))        
b=int(input("enter the b value :"))
small=min(a,b)               #take the samllest value from a,b .why we take min value mean takes low time to execute code .
for i in range(1,small+1):
    if a%i==0 and b%i==0:        #divide by both a and b .which one is satisify both condition .  
        gcd=i        #stores the gcd value 
print("gcd of and b is",gcd)


