a=[1,2,3,4,5]
rev=[]
for i in range(len(a)-1,-1,-1):
    rev.append(a[i])
print(rev)

"""
Iteration 1:
i = 4 → a[4] = 5
rev.append(5) → rev = [5]

Iteration 2:
i = 3 → a[3] = 4
rev.append(4) → rev = [5, 4]

Iteration 3:
i = 2 → a[2] = 3
rev.append(3) → rev = [5, 4, 3]

Iteration 4:
i = 1 → a[1] = 2
rev.append(2) → rev = [5, 4, 3, 2]

Iteration 5:
i = 0 → a[0] = 1
rev.append(1) → rev = [5, 4, 3, 2, 1]
"""
