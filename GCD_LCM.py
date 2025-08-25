#GCD
a=int(input("enter the a value :"))        
b=int(input("enter the b value :"))
small=min(a,b)               #take the samllest value from a,b .why we take min value mean takes low time to execute code .
for i in range(1,small+1):
    if a%i==0 and b%i==0:        #divide by both a and b .which one is satisify both condition .  
        gcd=i        #stores the gcd value 
print("gcd of and b is",gcd)

#LCM
a=int(input("enter the number:"))
b=int(input("enter the number:"))
large=max(a,b)        #get a large number 
while True:
    if large%a==0 and large%b==0:        
        break
    large+=max(a,b)        #increment the large value 
print("the LCM is",large)
