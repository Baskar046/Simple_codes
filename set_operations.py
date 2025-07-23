st=set(map(int,input("enter the elements").split()))
i=int(input("enter the elements to insert:"))
r=int(input("enter the elements to remove:"))
for u in sorted(st):
    print(u,end=" ")
print()

st.add(i)       #add items in st and sorted
for a in sorted(st):
    print(a,end=" ")
print()     #print empty line

st.remove(r)        #remove the items and sorted
for ve in sorted(st):
    print(ve,end=" ")
print()
print(sum(st))