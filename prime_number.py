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
