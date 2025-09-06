#finding the comon elements in the list
a=[1,2,3,4]
b=[5,6,7,1,2]
common=set(a) &set(b)
if common:
    print("common elements",common)
else:
    print("not common elements from this list")
