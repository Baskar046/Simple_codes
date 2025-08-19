# printing number pattern
n = int(input("enter the number:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# printing the star pattern
for i in range(1, 6):
    for j in range(1, i):
        print("*", end="")
    print()

#square wall pattern
n=int(input())
for i in range(n):
    print("*",end=" ")
print()
for i in range(n-2):
    print("*",end=" ")
    for j in range(n-2):
        print(" ",end=" ")
    print("*")
for i in range(n):
    print("*",end=" ")

#downwards triangle
class Solution:
    def printPattern(self,n):
        for i in range(n):
            for j in range(n-i):
                print("*",end=" ")
            print()

obj=Solution()
obj.printPattern(n=int(input()))

#downwards triangle 
n=5
for i in range(n,0,-1):
    for j in range(i):
        print(j,end=" ")
    print()

#triangle pattern
n = 9

for i in range(n):
    for j in range(n):
        # Print "*" only for the first column, or when row and column are same (diagonal), or for the last row
        if j == 0 or i == j or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
