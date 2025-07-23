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