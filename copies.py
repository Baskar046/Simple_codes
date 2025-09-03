import copy
a=[[1,2],[3.4]]
b=copy.copy(a)      #shallow copy
b[0][1]=3
print("original copy",a)
print(id(a[0]))
print("shallow copy",b)
print(id(b[0]))
Shallow copy: Copies the container, but shares nested objects.

a=[[1,2],[3.4]]
b=copy.deepcopy(a)  #deep copy
b[1][0]=9
print("original copy",a)
print(id(a[0]))
print("deep copy",b)
print(id(b[0]))
Deep copy: Copies the container and all nested objects.
