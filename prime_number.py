n = int(input("enter the number:"))
def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("it's not a prime number")
                break
        else:
            print("it's prime number")
    else:
        print("enter the valid number")
prime(n)


#finding next prime number
n=int(input())      #when input is 7
n=n+1               # it's become 8
while True:        #run till condition false
    for i in range(2,n):    #range is(2,n-1) so it's (2,3,4,5,6,7)
        if n%i==0:          #(8%2==0) condition condition is true
            break   #break condition works
    else:
        print(n)        #when
        break
    n+=1        #increment of n


#finding next prime number
def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
n = int(input())
num = n + 1  # when n=17 means num=18 check prime function and check again
while True:
    if prime(num):
        print(num)
        break
    num += 1


#print prime number series
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
num=2
i=0
while i<n+1:
    if prime(num):
        print(num,end=" ")
    i+=1
    num+=1


#prime number calculation
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    return False

def calculation(n1):
    for i in range(2,n1+1):
        if prime(i):
            x=i
            while n1%x==0:
                print(i)
                x*=i

n1=int(input())
calculation(n1)
