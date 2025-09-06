#finding the missing value from the list
a=[1,2,3,4]
b=[5,6,7,1,2]
#missing value in a
c={i for i in a if i not in b}
print(c)
